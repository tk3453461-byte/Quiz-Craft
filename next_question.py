import streamlit as st


def move_to_next():

    st.session_state.current_question += 1

    st.rerun()
