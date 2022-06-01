import random
import prompt


def guess_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number = random.randint(1, 30)

    def is_prime():
        if number < 2:
            return 'no'
        divider = 2
        while divider <= number / 2:
            if number % divider == 0:
                return 'no'
            divider = divider + 1
        return 'yes'

    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    correct_answer = is_prime()
    return [answer, correct_answer]


def game():
    return guess_prime()
