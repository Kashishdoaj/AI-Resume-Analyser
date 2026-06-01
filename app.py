import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.markdown("""
Welcome to the AI Resume Analyzer.

Use the sidebar to:

- Resume Preview
- Single Resume Analysis
- Multiple Resume Comparison
""")