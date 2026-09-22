import streamlit as st

from answer_handler import save_answer
from next_question import move_to_next
from result_display import show_result


def display_quiz():

    if not st.session_state.quiz:
        return

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    i = st.session_state.current_question

    quiz = st.session_state.quiz

    q = quiz[i]

    total = len(quiz)

    st.markdown(
        f"""
        <div style="
            color:#aeb6d4;
            font-size:15px;
            margin-bottom:8px;
        ">
        Question {i + 1} of {total}
        </div>
        """,
        unsafe_allow_html=True
    )

    from progress_bar import show_progress

    show_progress(i, total)

    st.markdown(
        f"""
        <div class="question-box">
        ❓ {q["question"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.radio(
        "Choose your answer:",
        q["options"],
        index=None,
        key=f"question_{i}"
    )

    if st.button("➡️ Next Question"):

        if answer is not None:

            save_answer(i, answer)

            if i < total - 1:

                move_to_next()

            else:

                st.success(
                    "🎯 This is the last question. "
                    "Click Submit Quiz!"
                )

        else:

            st.warning(
                "⚠️ Please choose your answer first."
            )

    if st.button("🏆 Submit Quiz"):

        show_result()

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )
