import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    st.session_state.resume_text = text

    st.success(
        "Resume uploaded successfully."
    )

    st.info(
        "Use the left sidebar to open Resume Preview."
    )