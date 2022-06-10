import random


def question():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


RANGE_BEGIN = 1
RANGE_END = 30

def create_task():
    task = random.randint(RANGE_BEGIN, RANGE_END)
    return task


def is_prime(task):
        if task < 2:
            return False
        divider = 2
        while divider <= task / 2:
            if task % divider == 0:
                return False
            divider = divider + 1
        return True


def game():
    task = create_task()
    if is_prime(task):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return task, correct_answer
