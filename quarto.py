import game
import board
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--board",
        help="The board state"
    )
    parser.add_argument(
        "-p",
        "--piece",
        help="The piece you were given"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-i",
        "--interactive",
        help="Play your game and interact with the solver",
        action="store_true"
    )
    group.add_argument(
        "-spi",
        "--solve-piece",
        help="Suggest a piece to give to the opponent",
        action="store_true"
    )
    group.add_argument(
        "-spo",
        "--solve-position",
        help="Suggest where to put the piece you were given",
        action="store_true"
    )
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
