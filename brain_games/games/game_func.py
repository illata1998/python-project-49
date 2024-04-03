import prompt
from brain_games.games.welcome_func import welcome_user


def game_engine(question):
    MAX_ATTEMPT_COUNT = 3
    attempt_count = 0
    name = welcome_user()
    while attempt_count < MAX_ATTEMPT_COUNT:
        correct_answer = question(attempt_count)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            attempt_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if attempt_count == MAX_ATTEMPT_COUNT:
        print(f'Congratulations, {name}!')