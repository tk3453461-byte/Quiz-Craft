import streamlit as st

from login import login
from signup import signup


def authentication_page():

    st.markdown(
        """
        <div class="quiz-logo">🧠</div>

        <div class="quiz-subtitle">
            QuizCraft
        </div>

        <div class="quiz-description">
            Smart quiz generator for your study material
        </div>
        """,
        unsafe_allow_html=True
    )

    page = st.radio(
        "Choose an option",
        ["Login", "Sign Up"],
        horizontal=True
    )

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    if page == "Login":

        st.markdown(
            '<div class="section-title">🔐 Welcome Back</div>',
            unsafe_allow_html=True
        )

        login()

    else:

        st.markdown(
            '<div class="section-title">✨ Create your account</div>',
            unsafe_allow_html=True
        )

        signup()

    st.markdown("</div>", unsafe_allow_html=True)
