import prompt


ROUND_QUANTITY = 3


def load_game(game, question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question())
    for i in range(ROUND_QUANTITY):
        task, correct_answer = game()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i = i + 1
            if i == ROUND_QUANTITY:
                print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
