import streamlit as st

from check_user import check_user


def login():

    username = st.text_input(
        "Username",
        key="login_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("✨ Login"):

        user = check_user(
            username,
            password
        )

        if user:

            st.session_state.logged_in = True
            st.session_state.user_name = user[0]

            st.success(
                "🎉 Login successful!"
            )

            st.rerun()

        else:

            st.error(
                "Invalid username or password."
            )
