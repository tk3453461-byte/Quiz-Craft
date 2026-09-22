import streamlit as st

from pdf_extractor import extract_text_from_pdf
from text_cleaner import clean_text


def study_material_section():

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">📄 Choose your input</div>',
        unsafe_allow_html=True
    )

    input_type = st.radio(
        "How do you want to provide your study material?",
        ["upload PDF", "Enter text"],
        horizontal=True
    )

    if (
        st.session_state.last_input_type
        != input_type
    ):

        st.session_state.quiz = None
        st.session_state.current_question = 0
        st.session_state.cleaned_text = ""

        st.session_state.last_input_type = input_type

    if input_type == "upload PDF":

        pdf_file = st.file_uploader(
            "Upload your PDF",
            type=["pdf"]
        )

        if pdf_file:

            extracted_text = extract_text_from_pdf(
                pdf_file
            )

            cleaned_text = clean_text(
                extracted_text
            )

            st.session_state.cleaned_text = cleaned_text

            st.success(
                "✅ PDF uploaded successfully!"
            )

            with st.expander(
                "👀 View processed text"
            ):

                st.write(cleaned_text)

    else:

        text = st.text_area(
            "Enter your study material",
            height=200,
            placeholder="Paste or type your study material here..."
        )

        if st.button("⚡ Process Text"):

            if text:

                cleaned_text = clean_text(text)

                st.session_state.cleaned_text = cleaned_text

                st.success(
                    "✅ Text processed successfully!"
                )

                with st.expander(
                    "👀 View processed text"
                ):

                    st.write(cleaned_text)

            else:

                st.error(
                    "Please enter some text first."
                )

    st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.cleaned_text
