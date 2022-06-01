from brain_games.games.progression import game
from brain_games.load_game import load_game


def main():
    print('Welcome to the Brain Games!')
    return load_game(game)


if __name__ == '__main__':
    main()
