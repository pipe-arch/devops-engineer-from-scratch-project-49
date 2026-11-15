"""`brain-even` entry point."""

from brain_games import engine
from brain_games.games import even


def main() -> None:
    engine.run_game(even)


if __name__ == "__main__":
    main()
