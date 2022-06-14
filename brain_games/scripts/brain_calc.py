#!/usr/bin/python
import brain_games.games.calc as calc
from brain_games.engine import engine


def main():
    engine(calc.get_task_and_answer, calc.game_rules)


if __name__ == '__main__':
    main()
