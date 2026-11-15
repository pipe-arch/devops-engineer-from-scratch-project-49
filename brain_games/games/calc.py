"""Calculator game"""

import random

RULES = "What is the result of the expression?"

MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATORS = ("+", "-", "*")


def calculate(left: int, right: int, operator: str) -> int:
    match operator:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
    raise ValueError(f"Unknown operator: {operator}")


def generate_round() -> tuple[str, str]:
    left = random.randint(MIN_NUMBER, MAX_NUMBER)
    right = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)
    question = f"{left} {operator} {right}"
    return question, str(calculate(left, right, operator))
