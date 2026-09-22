import re


def clean_text(text):

    if not text:
        return ""

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    text = re.sub(
        r"[^\x00-\x7F]+",
        " ",
        text
    )

    return text.strip()
