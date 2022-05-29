import prompt
import random
import math


def gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {number1} and {number2}')
    ans = prompt.string('Your answer: ')
    correct_ans = math.gcd(number1, number2)
    return [int(ans), correct_ans]


def game():
    return gcd()
