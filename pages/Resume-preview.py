import streamlit as st

st.title("📄 Resume Preview")

if "resume_text" in st.session_state:

    st.text_area(
        "Extracted Resume",
        st.session_state.resume_text,
        height=500
    )

else:

    st.warning(
        "Upload a resume first."
    )