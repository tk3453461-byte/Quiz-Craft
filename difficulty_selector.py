import streamlit as st


def select_difficulty():

    st.markdown(
        "### 🎯 Select Difficulty"
    )

    return st.radio(
        "Choose your difficulty level",
        [
            "Easy",
            "Medium",
            "Hard"
        ],
        horizontal=True
    )
