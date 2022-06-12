#!/usr/bin/python
from brain_games.games.gcd import game, question
from brain_games.load_game import greet_user, run


def main():
    run(game, greet_user(question))


if __name__ == '__main__':
    main()
