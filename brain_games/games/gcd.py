import prompt
import random
import math


def question():
    print('Find the greatest common divisor of given numbers.')


def game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print(f'Question: {number1} {number2}')
    ans = prompt.string('Your answer: ')
    correct_ans = math.gcd(number1, number2)
    return [int(ans), correct_ans]
