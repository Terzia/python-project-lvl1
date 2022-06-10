import random


RANGE_BEGIN = 1
RANGE_END = 1000


def question():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def create_task():
    task = random.randint(RANGE_BEGIN, RANGE_END)
    return task


def is_even(task):
    return task % 2 == 0


def game():
    task = create_task()
    if is_even(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return task, correct_answer
