#!/usr/bin/python
from brain_games.games.even import guess_even
from brain_games.load_game import load_game


def main():
    print('Welcome to the Brain Games!')
    return load_game(guess_even)


if __name__ == '__main__':
    main()
