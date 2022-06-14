import prompt


ROUND_QUANTITY = 3


def engine(set_task_and_answer, QUESTION):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(QUESTION)
    count = 0
    while count < ROUND_QUANTITY:
        task, correct_answer = set_task_and_answer()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')
        count = count + 1
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        if count == ROUND_QUANTITY:
            print(f"Congratulations, {name}!")
