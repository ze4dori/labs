from game.src.cli import welcome_user
from game.src.game_engine import run_game
from game.src.games.nok import generate_numbers
from game.src.games.progression import generate_geometric_progression

def main():
    name = welcome_user()

    print("Let's play LCM game!")
    run_game(generate_numbers, name)

    print(f"\nNext up, the Progression game!")
    run_game(generate_geometric_progression, name)


if __name__ == '__main__':
    main()
