import random
import prompt


def progression():
    i = random.randint(1, 10)
    step = random.randint(1, 10)
    size = 9
    count = 0
    lst = []
    while count <= size:
        i = i + step
        lst.append(i)
        count = count + 1
    index = random.randint(0, size - 1)
    correct_answer = lst[index]
    lst.pop(index)
    lst.insert(index, '..')
    sequence = ' '.join(map(str, lst))
    print('What number is missing in the progression?')
    print(f'Question: {sequence}')
    ans = prompt.string('Your answer: ')
    return [int(ans), correct_answer]


def game():
    return progression()
