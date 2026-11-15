"""Prime game"""

import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def generate_round() -> tuple[str, str]:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = "yes" if is_prime(number) else "no"
    return str(number), answer
