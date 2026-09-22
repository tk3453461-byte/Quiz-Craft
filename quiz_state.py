import streamlit as st


def initialize_quiz_state():

    if "quiz" not in st.session_state:
        st.session_state.quiz = None

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}
