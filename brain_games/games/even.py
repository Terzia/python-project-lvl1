import random


RANGE_BEGIN = 1
RANGE_END = 1000


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(task):
    return task % 2 == 0


def get_task_and_answer():
    task = random.randint(RANGE_BEGIN, RANGE_END)
    if is_even(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return task, correct_answer
