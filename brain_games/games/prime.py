from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number == 2:
        return True
    if number <= 1 or number % 2 == 0:
        return False
    return not any(number % i == 0 for i in range(3, int(number ** 0.5) + 1, 2))


def generate_round():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
