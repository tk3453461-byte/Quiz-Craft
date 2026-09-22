import streamlit as st


def select_question_count():

    return st.number_input(
        "How many Questions do you want?",
        min_value=5,
        max_value=30,
        value=10,
        step=1
    )
