import streamlit as st

st.title("📄 Resume Preview")

if "resume_text" not in st.session_state:

    st.warning(
        "Please upload a resume first."
    )

else:

    st.write(
        st.session_state.resume_text
    )