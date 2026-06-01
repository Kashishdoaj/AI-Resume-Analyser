import streamlit as st
from utils.pdf_reader import extract_pdf_text

st.title("🤖 Single Resume Analysis")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    text = extract_pdf_text(
        uploaded_file
    )

    st.session_state.resume_text = text

    st.success(
        "Resume uploaded successfully."
    )

    st.subheader("Resume Preview")

    st.text_area(
        "",
        text,
        height=300
    )

    # Your ATS logic goes here