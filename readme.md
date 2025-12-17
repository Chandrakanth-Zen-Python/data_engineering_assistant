# 🧠 GenAI Data Engineering Assistant (RAG-based)

A **production-grade GenAI application** that demonstrates how Large Language Models (LLMs) can be applied to **real-world Data Engineering workflows** using a **Retrieval-Augmented Generation (RAG)** architecture.

This project is designed to showcase **Senior / Lead Data Engineering skills** and is suitable as a **live portfolio project** for job applications.

---

## 🚀 What This Project Does

The GenAI Data Engineering Assistant helps data engineers and analytics teams to:

* ✅ Generate **optimized SQL** from business questions
* ✅ Explain **dbt models and data transformations**
* ✅ Identify **data quality issues** and suggest dbt tests
* ✅ Recommend **performance and modeling optimizations**

Unlike toy demos, this project mirrors **enterprise data platform use cases**.

---

## 🏗️ Architecture Overview

```
Documents (SQL, dbt, Markdown)
        ↓
   Text Ingestion
        ↓
 OpenAI Embeddings
        ↓
   FAISS Vector Store
        ↓
 Context Retrieval (RAG)
        ↓
 OpenAI LLM (GPT-4o-mini)
        ↓
  Streamlit Web UI
```

**Key Design Principles**:

* Separation of ingestion and retrieval
* Vector-based semantic search
* Stateless UI with backend intelligence
* Secure API key management

---

## 🧰 Technology Stack

| Layer      | Technology                 |
| ---------- | -------------------------- |
| Language   | Python 3.10+               |
| LLM        | OpenAI GPT-4o-mini         |
| Embeddings | text-embedding-3-small     |
| Vector DB  | FAISS                      |
| UI         | Streamlit                  |
| Secrets    | dotenv / Streamlit Secrets |

---

## 📁 Project Structure

```
.
├── app.py               # Streamlit UI
├── ingest.py            # Document ingestion & vector indexing
├── rag.py               # Retrieval + LLM logic
├── prompts.py           # System & task prompts
├── requirements.txt
├── sample_data/         # Sample dbt/SQL/Docs
│   ├── models.md
│   ├── sample_sql.sql
│   └── dbt_project.yml
├── index.faiss          # FAISS index (generated)
├── docs.pkl             # Raw documents (generated)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2️⃣ Configure OpenAI API Key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

Add `.env` to `.gitignore`:

```txt
.env
```

For Streamlit deployments, use:

```
.streamlit/secrets.toml
```

```toml
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

---

### 3️⃣ Ingest Documents

Run the ingestion pipeline to create embeddings and index:

```bash
python ingest.py
```

Expected output:

```text
✅ Indexed X documents with dimension 1536
```

This generates:

* `index.faiss`
* `docs.pkl`

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

Open browser at:

```
http://localhost:8501
```

---

## 🧪 Sample Questions to Try

* "Generate SQL to calculate monthly revenue by customer"
* "Explain the dbt model for orders"
* "What data quality issues might exist in the orders table?"
* "Suggest Snowflake performance optimizations"

---

## 🔐 Security & Best Practices

* API keys are **never hardcoded**
* Secrets managed via environment variables
* Vector embeddings stored locally (no PII)
* Defensive checks for missing configs

---

## 📈 Why This Project Matters

This project demonstrates:

* ✔️ Practical GenAI (RAG) implementation
* ✔️ Strong Data Engineering fundamentals
* ✔️ Production-level Python practices
* ✔️ System design and architectural thinking
* ✔️ AI-readiness for modern data platforms

It is specifically aligned with:

* Senior / Lead Data Engineer roles
* AI / ML Data Engineer roles
* Platform & Analytics Engineering teams

---

## 🚀 Future Enhancements

* Token-aware document chunking
* dbt `manifest.json` ingestion
* SQL execution against Snowflake/BigQuery
* Caching for reduced LLM cost
* Authentication & role-based access

---

## 👤 Author

**Chandrakanth Karunakaran**
Lead Data Engineer | Cloud & GenAI Platforms

---

## 🏷️ Resume / Naukri Summary Snippet

```text
Built a GenAI-powered Data Engineering Assistant using RAG architecture to help data engineers generate SQL, explain dbt models, and identify data quality issues. Implemented using OpenAI embeddings, FAISS vector search, and Streamlit UI.
```

---

⭐ If you are a recruiter or hiring manager, this project represents real-world, production-aligned GenAI engineering work.
