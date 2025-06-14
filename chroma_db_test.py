from chromadb import PersistentClient

CHROMA_DIR = "chroma_dbs/course_files"
CHROMA_COLLECTION_NAME = "course"

client = PersistentClient(path=CHROMA_DIR)
collection = client.get_collection(name=CHROMA_COLLECTION_NAME)

print("🔢 Total documents in collection:", collection.count())
