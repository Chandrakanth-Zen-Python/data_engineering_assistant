import streamlit as st
from rag import ask_llm

st.set_page_config(page_title="GenAI Data Engineering Assistant")

st.title("🧠 GenAI Data Engineering Assistant")

query = st.text_area(
    "Ask a question (SQL, dbt models, data quality, optimization):"
)

if st.button("Ask"):
    with st.spinner("Thinking like a Senior Data Engineer..."):
        response = ask_llm(query)
        st.markdown("### ✅ Response")
        st.write(response)
