import os
import time
import base64
import io
import json
from typing import Optional, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image
from openai import OpenAI
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from chromadb import PersistentClient
from dotenv import load_dotenv

load_dotenv()

# === CONFIG ===
AZURE_ENDPOINT = "https://tds-ocr.cognitiveservices.azure.com/"
AZURE_KEY = os.getenv("AZURE_KEY")
CHROMA_PATH = "chroma_dbs/course_files"
CHROMA_COLLECTION_NAME = "course"
EMBED_MODEL = "text-embedding-3-small"

# === FastAPI Setup ===
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# === Clients ===
ocr_client = ComputerVisionClient(AZURE_ENDPOINT, CognitiveServicesCredentials(AZURE_KEY))

groq_client = OpenAI(
    api_key=os.getenv("GROQ_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

embedding_client = OpenAI(
    api_key=os.getenv("AIPIPE_KEY"),
    base_url="https://aipipe.org/openai/v1"
)

# === Chroma Setup (READ-ONLY) ===
chroma_client = PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_collection(name=CHROMA_COLLECTION_NAME)

# === Models ===
class Link(BaseModel):
    url: str
    text: str

class TAResponse(BaseModel):
    answer: str
    links: List[Link]

class QuestionInput(BaseModel):
    question: str
    image: Optional[str] = None  # base64 string

# === Embedding Function ===
def embed_text(text: str):
    response = embedding_client.embeddings.create(
        input=[text],
        model=EMBED_MODEL
    )
    return response.data[0].embedding

# === OCR Function ===
async def extract_text_from_image(image_base64: str) -> str:
    try:
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data)).convert("RGB")

        image_io = io.BytesIO()
        image.save(image_io, format="PNG")
        image_io.seek(0)

        read_response = ocr_client.read_in_stream(image_io, raw=True)
        operation_id = read_response.headers["Operation-Location"].split("/")[-1]

        # Poll for result
        for _ in range(30):
            result = ocr_client.get_read_result(operation_id)
            if result.status not in ['notStarted', 'running']:
                break
            time.sleep(0.5)

        if result.status == OperationStatusCodes.succeeded:
            return " ".join([line.text for page in result.analyze_result.read_results for line in page.lines])
        return ""
    except Exception as e:
        print(f"[OCR ERROR] {e}")
        return ""

@app.get("/")
def root():
    return {"message": "TDS Virtual TA is running."}

@app.get("/api/")
def root_api():
    return {"message": "TDS Virtual TA is running."}

# === Main Endpoint ===
# === Main Endpoint ===
@app.post("/api/", response_model=TAResponse)
async def virtual_ta(input: QuestionInput):
    total_start = time.time()

    question_text = input.question.strip()
    if input.image:
        ocr_text = await extract_text_from_image(input.image)
        question_text += f"\n\nExtracted text from image:\n{ocr_text}"

    print("[QUESTION]", question_text)
    
    # Embed and search
    embed_start = time.time()
    embedded_query = embed_text(question_text)
    results = collection.query(query_embeddings=[embedded_query], n_results=2)
    embed_end = time.time()

    if not results['documents'] or not results['documents'][0]:
        print("[WARNING] No relevant documents found in ChromaDB.")
        return TAResponse(
            answer="Sorry, I couldn't find any relevant information in the course materials.",
            links=[]
        )

    documents = results['documents'][0]
    metadatas = results['metadatas'][0]

    search_info = "\n".join(
        [f"Snippet {i+1}: {doc}\nLink: {meta['url']}" for i, (doc, meta) in enumerate(zip(documents, metadatas))]
    )
    print("[SEARCH RESULTS]\n", search_info)

    # LLM Answer
    llm_start = time.time()
    prompt = f"""
Answer the user's question based on the following context. Return your output as a JSON object with this format:
{{\n  "answer": "...",\n  "links": [{{"url": "...", "text": "..."}}, ...]\n}}

Question: {question_text}

Context:
{search_info}
    """

    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that gives answers in structured JSON format."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    llm_end = time.time()
    total_end = time.time()

    print(f"[TIMING] Embedding: {embed_end - embed_start:.2f}s | LLM: {llm_end - llm_start:.2f}s | Total: {total_end - total_start:.2f}s")

    try:
        parsed = json.loads(response.choices[0].message.content)
        return TAResponse(**parsed)
    except Exception as e:
        print("[JSON PARSE ERROR]", e)
        print("[RAW LLM RESPONSE]", response.choices[0].message.content)
        return TAResponse(answer="Answer generation failed.", links=[])