#!/usr/bin/python
import brain_games.games.progression as progression
from brain_games.engine import engine


def main():
    engine(progression.get_task_and_answer, progression.game_rules)


if __name__ == '__main__':
    main()
