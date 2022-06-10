import random


RANGE_BEGIN = 1
RANGE_END = 10
SIZE = 9
init_term = random.randint(RANGE_BEGIN, RANGE_END)
difference = random.randint(RANGE_BEGIN, RANGE_END)
index = random.randint(0, SIZE - 1)

def question():
    print('What number is missing in the progression?')


def sequence(init_term, difference):
    count = 1
    i = init_term
    lst = [init_term,]
    while count <= SIZE:
        i = i + difference
        lst.append(i)
        count = count + 1
    return lst


def create_task(index):
    lst = sequence(init_term, difference)
    lst.pop(index)
    lst.insert(index, '..')
    task = ' '.join(map(str, lst))
    return task


def game():
    task = create_task(index)
    lst = sequence(init_term, difference)
    correct_answer = str(lst[index])
    return task, correct_answer
