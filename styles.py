import streamlit as st


def apply_styles():

    st.markdown(
        """
        <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
        );

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(125, 60, 255, 0.20),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 90% 20%,
                    rgba(0, 150, 255, 0.18),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 50% 90%,
                    rgba(180, 40, 255, 0.15),
                    transparent 30%
                ),
                #050817 !important;

            font-family: 'Inter', sans-serif !important;
            color: white !important;
        }

        .block-container {
            padding-top: 2rem !important;
            max-width: 1150px !important;
        }

        p, span, label, div {
            font-family: 'Inter', sans-serif;
        }

        h1 {
            text-align: center !important;
            font-size: 55px !important;
            font-weight: 800 !important;

            background: linear-gradient(
                90deg,
                #ffffff,
                #b66cff,
                #6c9cff
            );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        h2, h3, h4 {
            color: #ffffff !important;
            font-weight: 700 !important;
        }

        .quiz-logo {
            text-align: center;
            font-size: 62px;
            margin-bottom: -10px;
        }

        .quiz-subtitle {
            text-align: center;
            font-size: 28px;
            font-weight: 700;

            background: linear-gradient(
                90deg,
                #d28cff,
                #7ca8ff
            );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .quiz-description {
            text-align: center;
            color: #aeb6d4 !important;
            font-size: 17px;
            margin-bottom: 35px;
        }

        .glass-card {
            background: rgba(12, 17, 45, 0.78);
            border: 1px solid rgba(145, 100, 255, 0.35);
            border-radius: 24px;
            padding: 30px;
            box-shadow:
                0 0 30px rgba(101, 55, 255, 0.12),
                inset 0 0 25px rgba(255,255,255,0.02);
            margin-bottom: 25px;
        }

        .section-title {
            font-size: 25px;
            font-weight: 700;
            color: white;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            padding-bottom: 15px;
            margin-bottom: 25px;
        }

        .stRadio label {
            color: #dce2ff !important;
            font-weight: 500 !important;
        }

        .stRadio [role="radiogroup"] {
            gap: 12px;
        }

        .stTextInput input,
        .stTextArea textarea,
        .stNumberInput input {

            background: rgba(15, 22, 55, 0.9) !important;
            color: white !important;
            border: 1px solid rgba(130, 100, 255, 0.35) !important;
            border-radius: 12px !important;
            padding: 12px !important;
        }

        input::placeholder,
        textarea::placeholder {
            color: #8790b2 !important;
        }

        .stSelectbox > div > div {
            background: rgba(15, 22, 55, 0.9) !important;
            color: white !important;
            border: 1px solid rgba(130, 100, 255, 0.35) !important;
            border-radius: 12px !important;
        }

        [data-testid="stFileUploader"] {
            background: rgba(15, 22, 55, 0.7);
            border: 1px dashed #765cff;
            border-radius: 16px;
            padding: 15px;
        }

        .stButton > button {

            width: 100%;
            border: none !important;
            border-radius: 14px !important;
            padding: 13px 20px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            color: white !important;

            background: linear-gradient(
                90deg,
                #8a2be2,
                #5b7cff,
                #168cff
            ) !important;

            box-shadow:
                0 5px 20px rgba(91, 75, 255, 0.30);
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow:
                0 8px 30px rgba(116, 80, 255, 0.55);
        }

        .stNumberInput button {
            background: #171d45 !important;
            color: white !important;
            border: 1px solid #3e477c !important;
        }

        .stProgress > div > div > div {
            background: linear-gradient(
                90deg,
                #a33cff,
                #4e8cff
            ) !important;
        }

        .question-box {
            background:
                linear-gradient(
                    135deg,
                    rgba(115, 55, 255, 0.15),
                    rgba(30, 100, 255, 0.10)
                );

            border: 1px solid rgba(130, 100, 255, 0.35);
            border-radius: 18px;
            padding: 25px;
            margin: 20px 0;
            font-size: 22px;
            font-weight: 600;
            color: white;
        }

        [data-testid="stAlert"] {
            border-radius: 14px !important;
        }

        .login-card {
            max-width: 500px;
            margin: auto;
            background: rgba(12, 17, 45, 0.85);
            padding: 35px;
            border-radius: 25px;
            border: 1px solid rgba(140, 90, 255, 0.35);
        }

        .footer {
            text-align: center;
            color: #7f88a8;
            margin-top: 40px;
            font-size: 14px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
