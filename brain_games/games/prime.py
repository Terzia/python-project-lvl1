import random


RANGE_BEGIN = 1
RANGE_END = 30


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(task):
    if task < 2:
        return False
    divider = 2
    while divider <= task / 2:
        if task % divider == 0:
            return False
        divider = divider + 1
    return True


def get_task_and_answer():
    task = random.randint(RANGE_BEGIN, RANGE_END)
    if is_prime(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return task, correct_answer
