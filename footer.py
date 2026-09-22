import streamlit as st


def show_footer():

    st.markdown(
        """
        <div class="footer">

        🔒 Your study material is secure
        &nbsp; • &nbsp;

        🧠 QuizCraft
        &nbsp; • &nbsp;

        🚀 Keep Learning!

        </div>
        """,
        unsafe_allow_html=True
    )
