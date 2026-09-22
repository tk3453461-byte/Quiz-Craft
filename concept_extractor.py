import re


def extract_concepts(text):

    sentences = re.split(
        r"[.!?]",
        text
    )

    concepts = []

    patterns = [

        (
            "definition",
            r"^(.+?)\s+is\s+(?:a|an|the)\s+(.+)$"
        ),

        (
            "definition",
            r"^(.+?)\s+is\s+(.+)$"
        ),

        (
            "definition",
            r"^(.+?)\s+are\s+(.+)$"
        ),

        (
            "use",
            r"^(.+?)\s+is\s+used\s+for\s+(.+)$"
        ),

        (
            "use",
            r"^(.+?)\s+uses\s+(.+)$"
        ),

        (
            "support",
            r"^(.+?)\s+supports\s+(.+)$"
        ),

        (
            "provide",
            r"^(.+?)\s+provides\s+(.+)$"
        ),

        (
            "allow",
            r"^(.+?)\s+allows\s+(.+)$"
        ),

        (
            "help",
            r"^(.+?)\s+helps\s+(.+)$"
        )
    ]

    for sentence in sentences:

        sentence = re.sub(
            r"\s+",
            " ",
            sentence.strip()
        )

        if len(sentence.split()) < 4:
            continue

        for relation, pattern in patterns:

            match = re.match(
                pattern,
                sentence,
                re.IGNORECASE
            )

            if match:

                subject = match.group(1).strip()
                answer = match.group(2).strip()

                if (
                    len(subject.split()) <= 8
                    and len(answer.split()) >= 2
                ):

                    concepts.append(
                        {
                            "subject": subject,
                            "answer": answer,
                            "relation": relation
                        }
                    )

                    break

    return concepts
