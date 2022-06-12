from brain_games.games.progression import game, question
from brain_games.load_game import greet_user, run


def main():
    run(game, greet_user(question))


if __name__ == '__main__':
    main()
