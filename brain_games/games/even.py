import random
import prompt


def question():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game():
    number = random.randint(1, 1000)

    def is_even():
        if number % 2 == 0:
            return 'yes'
        else:
            return 'no'

    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    correct_answer = is_even()
    return [answer, correct_answer]
