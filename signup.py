import streamlit as st

from create_user import create_user


def signup():

    name = st.text_input("Name")

    username = st.text_input(
        "Username",
        key="signup_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="signup_password"
    )

    if st.button("🚀 Create Account"):

        if name and username and password:

            if create_user(
                name,
                username,
                password
            ):

                st.success(
                    "🎉 Account created successfully!"
                )

            else:

                st.error(
                    "Username already exists."
                )

        else:

            st.error(
                "Please fill all the fields."
            )
