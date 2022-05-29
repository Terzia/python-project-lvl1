import prompt
import random


def calc():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    op = random.choice(['+', '-', '*'])
    expression = str(number1) + ' ' + op + ' ' + str(number2)
    print('What is the result of the expression?')
    print(f'Question: {expression}')
    ans = prompt.string('Your answer: ')
    correct_ans = eval(expression)
    return [int(ans), correct_ans]


def game():
    return calc()