import game
import board
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--board",
        # TODO(brouxco): define how to describe the board state
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

    b = board.Board()

    if args.board:
        # TODO(brouxco): import the board state
        pass

    if args.piece:
        # TODO(brouxco): handle the piece
        pass

    if args.interactive:
        while (not b.is_move_losing()):
            score, piece = game.Game().monte_carlo(b, 1000)
            print("Your should give this piece to your opponent: {}".format(
                piece
            ))
            position = input("Where did the opponent put the piece (x,y): ")
            print(position)
            position = position.split(",")
            position = [int(x) for x in position]
            print(position)
            b.place(*position, piece)

            print(b)

            if b.is_move_losing():
                break

            given_piece = input("What piece did he give you: ")
            # TODO(brouxco): search for the best position on the board
            # and place it there
            position = input("Where do you want to put the piece (x,y): ")
            print(position)
            position = position.split(",")
            position = [int(x) for x in position]
            print(position)
            if not b.place(*position, given_piece):
                print("Impossible to place", given_piece, " here")
                # TODO(brouxco): ask again

    if args.solve_piece:
        print(*game.Game().monte_carlo(b, 1000))

    if args.solve_position:
        print(*game.Game().monte_carlo(b, 1000))


if __name__ == "__main__":
    main()
