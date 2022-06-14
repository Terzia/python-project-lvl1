import random


RANGE_BEGIN = 1
RANGE_END = 10
SIZE = 9


game_rules = 'What number is missing in the progression?'


def create_progression(init_term, difference):
    count = 1
    i = init_term
    progression = [init_term, ]
    while count <= SIZE:
        i = i + difference
        progression.append(i)
        count = count + 1
    return progression


def create_task(progression, missing_num_index):
    progression.pop(missing_num_index)
    progression.insert(missing_num_index, '..')
    task = ' '.join(map(str, progression))
    return task


def get_task_and_answer():
    init_term = random.randint(RANGE_BEGIN, RANGE_END)
    difference = random.randint(RANGE_BEGIN, RANGE_END)
    missing_num_index = random.randint(0, SIZE - 1)
    progression = create_progression(init_term, difference)
    correct_answer = str(progression[missing_num_index])
    task = create_task(progression, missing_num_index)
    return task, correct_answer
