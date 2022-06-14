#!/usr/bin/python
import brain_games.games.gcd as gcd
from brain_games.engine import engine


def main():
    engine(gcd.get_task_and_answer, gcd.game_rules)


if __name__ == '__main__':
    main()
