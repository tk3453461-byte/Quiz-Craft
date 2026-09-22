import random

from category_detector import get_category


def get_distractors(correct_answer, concepts):

    correct_category = get_category(
        correct_answer
    )

    candidates = []

    for concept in concepts:

        answer = concept["answer"].strip()

        if answer.lower() == correct_answer.lower():
            continue

        if get_category(answer) == correct_category:

            candidates.append(answer)

    random.shuffle(candidates)

    if len(candidates) < 3:

        for concept in concepts:

            answer = concept["answer"].strip()

            if answer.lower() == correct_answer.lower():
                continue

            if answer not in candidates:
                candidates.append(answer)

            if len(candidates) == 3:
                break

    result = []

    for answer in candidates:

        if answer.lower() != correct_answer.lower():

            if answer not in result:
                result.append(answer)

        if len(result) == 3:
            break

    return result
