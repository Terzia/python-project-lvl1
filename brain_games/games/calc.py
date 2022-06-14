import random


RANGE_BEGIN = 1
RANGE_END = 10
QUESTION = 'What is the result of the expression?'


def set_task_and_answer():
    number1 = random.randint(RANGE_BEGIN, RANGE_END)
    number2 = random.randint(RANGE_BEGIN, RANGE_END)
    op = random.choice(['+', '-', '*'])
    task = str(number1) + ' ' + op + ' ' + str(number2)
    correct_answer = str(eval(task))
    return task, correct_answer
