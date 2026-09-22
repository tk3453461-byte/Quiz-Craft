import streamlit as st


def initialize_session():

    defaults = {
        "logged_in": False,
        "user_name": "",
        "quiz": None,
        "current_question": 0,
        "user_answers": {},
        "cleaned_text": "",
        "input_type": "upload PDF",
        "last_input_type": "upload PDF"
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value
