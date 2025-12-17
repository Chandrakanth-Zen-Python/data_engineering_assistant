import streamlit as st
from rag import ask_llm
import time

MAX_REQUESTS = 10
WINDOW_SECONDS = 300  # 5 minutes

if "request_times" not in st.session_state:
    st.session_state.request_times = []


MAX_DAILY_QUERIES = 25

if "daily_count" not in st.session_state:
    st.session_state.daily_count = 0

if st.session_state.daily_count >= MAX_DAILY_QUERIES:
    st.warning("⚠️ Daily usage limit reached. Try again tomorrow.")
    st.stop()



st.set_page_config(page_title="GenAI Data Engineering Assistant")

st.title("🧠 GenAI Data Engineering Assistant")

query = st.text_area(
    "Ask a question (SQL, dbt models, data quality, optimization):"
)

def is_valid_de_prompt(prompt: str) -> bool:
    allowed_keywords = [
        "sql", "dbt", "data", "pipeline",
        "warehouse", "etl", "schema",
        "quality", "model", "snowflake"
    ]
    prompt_lower = prompt.lower()
    return any(keyword in prompt_lower for keyword in allowed_keywords)


if st.button("Ask"):
    now = time.time()

    # Remove old requests
    st.session_state.request_times = [
        t for t in st.session_state.request_times
        if now - t < WINDOW_SECONDS
    ]

    if len(st.session_state.request_times) >= MAX_REQUESTS:
        st.error("🚫 Rate limit exceeded. Please wait a few minutes.")
        st.stop()

    st.session_state.request_times.append(now)

    if not is_valid_de_prompt(query):
        st.error("❌ This assistant is restricted to Data Engineering queries only.")
        st.stop()
    
    MAX_PROMPT_LENGTH = 500  # characters

    if len(query) > MAX_PROMPT_LENGTH:
        st.error("❌ Query too long. Please be concise.")
        st.stop()



    with st.spinner("Thinking like a Senior Data Engineer..."):
        response = ask_llm(query)
        st.markdown("### ✅ Response")
        st.write(response)

