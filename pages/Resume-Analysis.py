import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

st.title("🧠 Resume Analysis")

if "resume_text" not in st.session_state:

    st.warning(
        "Please upload a resume first."
    )

else:

    text = st.session_state.resume_text

    if st.button("Analyze Resume"):

        prompt = f"""
        Analyze this resume.

        Give:
        1. Skills
        2. Strengths
        3. Weaknesses
        4. ATS Score

        Resume:
        {text}
        """

        with st.spinner(
            "Analyzing..."
        ):

            response = model.generate_content(
                prompt
            )

        st.markdown(
            response.text
        )