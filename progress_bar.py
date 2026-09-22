import streamlit as st


def show_progress(
    current_question,
    total_questions
):

    progress = (
        (current_question + 1)
        / total_questions
    )

    st.progress(progress)
