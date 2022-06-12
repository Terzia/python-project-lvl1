import random


RANGE_BEGIN = 1
RANGE_END = 10
SIZE = 9


def generate_numbers():
    init_term = random.randint(RANGE_BEGIN, RANGE_END)
    difference = random.randint(RANGE_BEGIN, RANGE_END)
    index = random.randint(0, SIZE - 1)
    return init_term, difference, index


def question():
    print('What number is missing in the progression?')


def sequence(init_term, difference):
    count = 1
    i = init_term
    lst = [init_term, ]
    while count <= SIZE:
        i = i + difference
        lst.append(i)
        count = count + 1
    return lst


def create_task(lst, index):
    lst.pop(index)
    lst.insert(index, '..')
    task = ' '.join(map(str, lst))
    return task


def game():
    init_term, difference, index = generate_numbers()
    lst = sequence(init_term, difference)
    correct_answer = str(lst[index])
    task = create_task(lst, index)
    return task, correct_answer
