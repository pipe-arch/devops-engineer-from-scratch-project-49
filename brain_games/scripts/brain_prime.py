"""`brain-prime` entry point."""

from brain_games import engine
from brain_games.games import prime


def main() -> None:
    engine.run_game(prime)


if __name__ == "__main__":
    main()
