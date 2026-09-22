import streamlit as st


def calculate_score():

    score = 0

    quiz = st.session_state.quiz
    answers = st.session_state.user_answers

    for index, question in enumerate(quiz):

        user_answer = answers.get(index)

        if user_answer == question["answer"]:

            score += 1

    total = len(quiz)

    wrong = total - score

    percentage = (
        score / total
    ) * 100 if total else 0

    return score, wrong, total, percentage
