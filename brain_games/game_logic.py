import random
import prompt


def guess_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):

        number = random.randint(1, 1000)

        def is_even():
            if number % 2 == 0:
                return 'yes'
            else:
                return 'no'

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if is_even() == answer:
            print('Correct!')
            i = i + 1
            if i == 3:
                print('Congratulations!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{is_even()}'")
            print(f"Let's try again, {name}!")
            break
