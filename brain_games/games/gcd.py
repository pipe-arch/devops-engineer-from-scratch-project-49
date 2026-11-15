"""GCD game"""

import random

RULES = "Find the greatest common divisor of given numbers."

MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd(first: int, second: int) -> int:
    while second:
        first, second = second, first % second
    return first


def generate_round() -> tuple[str, str]:
    first = random.randint(MIN_NUMBER, MAX_NUMBER)
    second = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{first} {second}"
    return question, str(gcd(first, second))
