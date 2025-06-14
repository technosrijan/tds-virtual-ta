import os
import glob
import uuid
import chromadb
from openai import OpenAI

# === Config ===
EMBED_MODEL = "text-embedding-3-small"
CHROMA_DIR = "chroma_dbs/course_files"
CHROMA_COLLECTION_NAME = "course"
MARKDOWN_DIR = "TDS_Course_Files"  # Directory with .md files

# === API SETUP (AI Pipe proxy) ===
client = OpenAI(
    api_key=os.getenv("AIPIPE_KEY"),
    base_url="https://aipipe.org/openai/v1"
)

# === Chroma DB Setup ===
chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = chroma_client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)

# === Embedding + Storing ===
def embed_text(text: str):
    response = client.embeddings.create(
        input=[text],
        model=EMBED_MODEL
    )
    return response.data[0].embedding

def process_markdown_files(directory: str):
    md_files = glob.glob(os.path.join(directory, "*.md"))
    print(f"Found {len(md_files)} markdown files.")

    for file_path in md_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        
        if not content:
            print(f"Skipping empty file: {file_path}")
            continue

        file_name = os.path.basename(file_path).replace(".md", "")
        url = f"https://tds.s-anand.net/#/{file_name}"
        doc_id = str(uuid.uuid4())

        try:
            embedding = embed_text(content)
            collection.add(
                ids=[doc_id],
                embeddings=[embedding],
                documents=[content],
                metadatas=[{"url": url}]
            )
            print(f"✅ Added: {file_name}")
        except Exception as e:
            print(f"❌ Failed on {file_name}: {e}")

# === Run ===
if __name__ == "__main__":
    process_markdown_files(MARKDOWN_DIR)