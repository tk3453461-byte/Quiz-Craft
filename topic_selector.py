import streamlit as st


def select_topic():

    return st.selectbox(
        "Select your topic",
        [
            "Python",
            "C programming",
            "Digital electronics",
            "Computer Networks",
            "Database",
            "Other"
        ]
    )
