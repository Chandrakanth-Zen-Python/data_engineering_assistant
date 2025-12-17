import os
import faiss
import pickle
import numpy as np
import streamlit as st
from openai import OpenAI
from prompts import SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()

# 🔐 Secure key loading (local + cloud)
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        api_key = st.secrets.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found")

    return OpenAI(api_key=api_key)

client = get_openai_client()

index = faiss.read_index("index.faiss")
docs = pickle.load(open("docs.pkl", "rb"))

def retrieve_context(query, k=2):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    vector = np.array(response.data[0].embedding).astype("float32")
    vector = vector.reshape(1, -1)

    D, I = index.search(vector, k)
    return "\n".join([docs[i] for i in I[0]])

def ask_llm(query):
    context = retrieve_context(query)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{query}"
            }
        ]
    )

    return completion.choices[0].message.content
