"""Command-line entry point: ``python -m bure``."""

import argparse
import os

from .difficulty import DIFFICULTIES
from .levels import LEVELS


def main() -> None:
    parser = argparse.ArgumentParser(prog="bure", description="BURE - an arcade math game.")
    parser.add_argument("--level", type=int, choices=range(1, len(LEVELS) + 1),
                        metavar=f"1-{len(LEVELS)}",
                        help="jump straight into this level, skipping the menu")
    parser.add_argument("--difficulty", choices=[d.key for d in DIFFICULTIES],
                        help="easy, normal or classic (default: last one you played)")
    parser.add_argument("--seed", type=int, help="random seed for the target numbers")
    args = parser.parse_args()

    os.environ.setdefault("SDL_VIDEO_CENTERED", "1")
    os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
    from .game import Game  # imported late so the env vars above take effect

    Game(start_level=args.level, seed=args.seed, difficulty=args.difficulty).run()


if __name__ == "__main__":
    main()
