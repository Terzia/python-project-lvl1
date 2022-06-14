#!/usr/bin/python
import brain_games.games.even as even
from brain_games.engine import engine


def main():
    engine(even.get_task_and_answer, even.game_rules)


if __name__ == '__main__':
    main()
