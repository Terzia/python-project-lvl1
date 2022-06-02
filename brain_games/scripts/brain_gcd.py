#!/usr/bin/python
from brain_games.games.gcd import game, question
from brain_games.load_game import load_game


def main():
    print('Welcome to the Brain Games!')
    return load_game(game, question)


if __name__ == '__main__':
    main()
