import os
import json
import uuid
import chromadb
from openai import OpenAI
from tqdm import tqdm

# === Config ===
EMBED_MODEL = "text-embedding-3-small"
CHROMA_DIR = "chroma_dbs/course_files"
CHROMA_COLLECTION_NAME = "course"
DISCOURSE_JSON_FILE = "tds_kb_scraped.json"

# === API SETUP (AI Pipe proxy) ===
client = OpenAI(
    api_key=os.getenv("AIPIPE_KEY"),
    base_url="https://aipipe.org/openai/v1"
)

# === Chroma DB Setup ===
chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = chroma_client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)

# === Embedding function ===
def embed_text(text: str):
    response = client.embeddings.create(
        input=[text],
        model=EMBED_MODEL
    )
    return response.data[0].embedding

# === Main processing ===
def process_discourse_json(json_file: str):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"📚 Processing {len(data)} threads...")

    for thread in tqdm(data):
        url = thread.get("url", "")
        posts = thread.get("posts", [])

        for post in posts:
            content = post.get("content", "").strip()
            if not content:
                continue

            doc_id = f"{thread['topic_id']}_{post['post_number']}"

            try:
                embedding = embed_text(content)
                collection.add(
                    ids=[doc_id],
                    embeddings=[embedding],
                    documents=[content],
                    metadatas=[{"url": url}]
                )
            except Exception as e:
                print(f"❌ Error adding {doc_id}: {e}")

# === Run ===
if __name__ == "__main__":
    process_discourse_json(DISCOURSE_JSON_FILE)