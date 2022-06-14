import random


RANGE_BEGIN = 1
RANGE_END = 10


game_rules = 'What is the result of the expression?'


def get_task_and_answer():
    number1 = random.randint(RANGE_BEGIN, RANGE_END)
    number2 = random.randint(RANGE_BEGIN, RANGE_END)
    op = random.choice(['+', '-', '*'])
    task = f'{str(number1)} {op} {str(number2)}'
    correct_answer = str(eval(task))
    return task, correct_answer
