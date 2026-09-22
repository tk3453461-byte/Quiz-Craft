import streamlit as st

from config import setup_page
from styles import apply_styles
from database_init import init_db
from session_state import initialize_session
from authentication import authentication_page
from input_handler import study_material_section
from topic_selector import select_topic
from difficulty_selector import select_difficulty
from question_counter import select_question_count
from quiz_generator import generate_quiz
from quiz_state import initialize_quiz_state
from question_display import display_quiz
from footer import show_footer


setup_page()
apply_styles()
init_db()
initialize_session()

if not st.session_state.logged_in:
    authentication_page()
    st.stop()

st.markdown(
    """
    <div class="quiz-logo">🧠</div>
    <h1>QuizCraft</h1>
    <div class="quiz-subtitle">
        ✨ Smart Quiz Generator
    </div>
    <div class="quiz-description">
        Generate quiz from your study material in seconds
    </div>
    """,
    unsafe_allow_html=True
)

number_of_questions = select_question_count()
topic = select_topic()
difficulty = select_difficulty()

cleaned_text = study_material_section()

initialize_quiz_state()

st.markdown(
    '<div class="glass-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🚀 Generate your Quiz</div>',
    unsafe_allow_html=True
)

if st.button("✨ Generate Quiz"):

    if not cleaned_text:
        st.warning(
            "⚠️ Please upload PDF or process your text first."
        )

    else:
        quiz = generate_quiz(
            cleaned_text,
            topic,
            difficulty,
            number_of_questions
        )

        st.session_state.quiz = quiz
        st.session_state.current_question = 0
        st.session_state.user_answers = {}

        if quiz:
            st.success("🎉 Quiz generated successfully!")
            st.rerun()
        else:
            st.warning(
                "Not enough information to generate questions."
            )

st.markdown("</div>", unsafe_allow_html=True)

display_quiz()

show_footer()
