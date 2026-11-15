"""Progression game"""

import random

RULES = "What number is missing in the progression?"

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 100
MIN_STEP = 1
MAX_STEP = 10
HIDDEN_MARK = ".."


def make_progression(start: int, step: int, length: int) -> list[int]:
    return [start + index * step for index in range(length)]


def generate_round() -> tuple[str, str]:
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = make_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    question = " ".join(
        HIDDEN_MARK if index == hidden_index else str(number)
        for index, number in enumerate(progression)
    )
    return question, str(correct_answer)
