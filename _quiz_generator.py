import random

from concept_extractor import extract_concepts
from distractor_generator import get_distractors
from question_maker import make_question


def generate_quiz(
    text,
    topic,
    difficulty,
    number_of_questions
):

    concepts = extract_concepts(text)

    if not concepts:
        return []

    random.shuffle(concepts)

    questions = []
    used_questions = set()
    used_subjects = set()

    for concept in concepts:

        if len(questions) >= number_of_questions:
            break

        subject = concept["subject"]
        answer = concept["answer"]
        relation = concept["relation"]

        subject_key = subject.lower().strip()

        if subject_key in used_subjects:
            continue

        distractors = get_distractors(
            answer,
            concepts
        )

        if len(distractors) < 3:
            continue

        question_text = make_question(
            subject,
            answer,
            relation,
            difficulty
        )

        question_key = (
            question_text.lower().strip()
        )

        if question_key in used_questions:
            continue

        options = [answer] + distractors

        random.shuffle(options)

        questions.append(
            {
                "question": question_text,
                "options": options,
                "answer": answer
            }
        )

        used_questions.add(question_key)
        used_subjects.add(subject_key)

    return questions
