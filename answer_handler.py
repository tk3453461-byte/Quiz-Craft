import streamlit as st


def save_answer(question_index, answer):

    st.session_state.user_answers[
        question_index
    ] = answer
