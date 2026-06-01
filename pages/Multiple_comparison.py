import streamlit as st
import pandas as pd
from utils.pdf_reader import extract_pdf_text

st.title("📊 Multiple Resume Comparison")

uploaded_files = st.file_uploader(
    "Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    resume_data = []

    for file in uploaded_files:

        text = extract_pdf_text(file)

        resume_data.append(
            {
                "Resume": file.name,
                "Word Count": len(text.split()),
                "Text": text
            }
        )

    st.success(
        f"{len(resume_data)} resumes uploaded."
    )

    df = pd.DataFrame(
        [
            {
                "Resume": r["Resume"],
                "Word Count": r["Word Count"]
            }
            for r in resume_data
        ]
    )

    st.subheader(
        "Comparison Table"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader(
        "Ranking"
    )

    ranking_df = df.sort_values(
        by="Word Count",
        ascending=False
    )

    ranking_df.insert(
        0,
        "Rank",
        range(
            1,
            len(ranking_df) + 1
        )
    )

    st.dataframe(
        ranking_df,
        use_container_width=True
    )

    tabs = st.tabs(
        [r["Resume"] for r in resume_data]
    )

    for tab, resume in zip(
        tabs,
        resume_data
    ):

        with tab:

            st.text_area(
                "Preview",
                resume["Text"],
                height=400
            )