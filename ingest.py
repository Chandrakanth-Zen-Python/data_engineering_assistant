import os
import faiss
import pickle
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def load_documents(path="sample_data"):
    texts = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if file_path.endswith((".md", ".sql", ".yml", ".txt")):
            with open(file_path, "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts

def create_embeddings(texts):
    embeddings = []
    for text in texts:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        embeddings.append(response.data[0].embedding)
    return embeddings

def build_vector_store():
    docs = load_documents()
    vectors = create_embeddings(docs)

    # 🔑 FIX: Convert list → NumPy array (float32)
    vectors_np = np.array(vectors).astype("float32")

    dim = vectors_np.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors_np)

    with open("docs.pkl", "wb") as f:
        pickle.dump(docs, f)

    faiss.write_index(index, "index.faiss")

    print(f"✅ Indexed {len(docs)} documents with dimension {dim}")

if __name__ == "__main__":
    build_vector_store()
