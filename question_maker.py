def make_question(
    subject,
    answer,
    relation,
    difficulty
):

    if difficulty == "Easy":

        if relation == "definition":
            return f"What is {subject}?"

        if relation == "use":
            return f"What is {subject} used for?"

        if relation == "support":
            return f"What does {subject} support?"

        if relation == "provide":
            return f"What does {subject} provide?"

        if relation == "allow":
            return f"What does {subject} allow?"

        if relation == "help":
            return f"What does {subject} help with?"

    elif difficulty == "Medium":

        if relation == "definition":
            return (
                f"Which of the following correctly "
                f"describes {subject}?"
            )

        if relation == "use":
            return (
                f"Which of the following is a use "
                f"of {subject}?"
            )

        if relation == "support":
            return (
                f"Which of the following is supported "
                f"by {subject}?"
            )

        if relation == "provide":
            return (
                f"Which of the following is provided "
                f"by {subject}?"
            )

        if relation == "allow":
            return (
                f"Which of the following is enabled "
                f"by {subject}?"
            )

        if relation == "help":
            return (
                f"Which of the following does "
                f"{subject} help with?"
            )

    else:

        if relation == "definition":
            return (
                f"Which statement best identifies "
                f"the nature of {subject}?"
            )

        if relation == "use":
            return (
                f"Which option best identifies the "
                f"purpose of {subject}?"
            )

        if relation == "support":
            return (
                f"Which option best identifies what "
                f"{subject} supports?"
            )

        if relation == "provide":
            return (
                f"Which option best identifies what "
                f"{subject} provides?"
            )

        if relation == "allow":
            return (
                f"Which option best identifies what "
                f"{subject} enables?"
            )

        if relation == "help":
            return (
                f"Which option best identifies the "
                f"function of {subject}?"
            )

    return (
        f"Which statement correctly describes "
        f"{subject}?"
    )
