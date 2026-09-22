import streamlit as st

from score_calculator import calculate_score


def show_result():

    score, wrong, total, percentage = (
        calculate_score()
    )

    st.balloons()

    st.success(
        f"🎉 Your Score: {score}/{total}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "✅ Correct",
            score
        )

    with col2:

        st.metric(
            "❌ Wrong",
            wrong
        )

    with col3:

        st.metric(
            "📊 Percentage",
            f"{percentage:.1f}%"
        )
