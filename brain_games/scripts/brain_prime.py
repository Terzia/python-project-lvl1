#!/usr/bin/python
import brain_games.games.prime as prime
from brain_games.engine import engine


def main():
    engine(prime.get_task_and_answer, prime.game_rules)


if __name__ == '__main__':
    main()
