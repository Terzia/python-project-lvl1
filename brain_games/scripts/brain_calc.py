#!/usr/bin/python
from brain_games.games.calc import set_task_and_answer, QUESTION
from brain_games.engine import engine


def main():
    engine(set_task_and_answer, QUESTION)


if __name__ == '__main__':
    main()
