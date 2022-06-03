import prompt


def load_game(game, question):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question())
    for i in range(3):
        answer, correct_answer = game()
        if answer == correct_answer:
            print('Correct!')
            i = i + 1
            if i == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
