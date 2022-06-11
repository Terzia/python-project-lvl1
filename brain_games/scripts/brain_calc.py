#!/usr/bin/python
from brain_games.games.calc import game, question
from brain_games.load_game import load_game


def main():
    load_game(game, question)


if __name__ == '__main__':
    main()
