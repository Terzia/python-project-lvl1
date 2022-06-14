import random
import math


RANGE_BEGIN = 1
RANGE_END = 100
QUESTION = 'Find the greatest common divisor of given numbers.'


def set_task_and_answer():
    number1 = random.randint(RANGE_BEGIN, RANGE_END)
    number2 = random.randint(RANGE_BEGIN, RANGE_END)
    task = str(number1) + ' ' + str(number2)
    correct_answer = str(math.gcd(number1, number2))
    return task, correct_answer
