import prompt


ROUND_QUANTITY = 3


def greet_user(question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question())
    return name


def check_answer(game, name):
    task, correct_answer = game()
    print(f'Question: {task}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(.")
        print(f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
    return answer == correct_answer


def run(game, name):
    count = 0
    while count < ROUND_QUANTITY:
        count = count + 1
        if not check_answer(game, name):
            break
        if count == 3:
            print(f'Congratulations, {name}!')
