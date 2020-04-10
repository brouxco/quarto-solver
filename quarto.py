import game
import piece
import board
import copy
import argparse

boards_scores = dict()


# return score, losing_piece
def find_losing_piece(board, opponent):
    if hash(board) in boards_scores:
        # BUG(brouxco): This may be invalid, the board score depends on the
        # player. We have to return the board score for the player
        return boards_scores[hash(board)]
    if board.is_move_losing():
        return 1 if opponent else -1, None
    if len(board.available_pieces) == 0:
        return 0, None
    original_board = copy.deepcopy(board)
    pieces_score = [0 for _ in original_board.available_pieces]
    if not opponent:
        for i, p in enumerate(original_board.available_pieces):
            for move in original_board.allowed_moves():
                board.place(*move, p)
                score, _ = find_losing_piece(board, True)
                pieces_score[i] += score
                board = copy.deepcopy(original_board)
        max_piece_index = pieces_score.index(max(pieces_score))
        boards_scores[hash(original_board)] = (
            pieces_score[max_piece_index],
            original_board.available_pieces[max_piece_index]
        )
    else:
        for i, p in enumerate(original_board.available_pieces):
            for move in original_board.allowed_moves():
                board.place(*move, p)
                score, _ = find_losing_piece(board, False)
                pieces_score[i] += score
                board = copy.deepcopy(original_board)
        min_piece_index = pieces_score.index(min(pieces_score))
        boards_scores[hash(original_board)] = (
            pieces_score[min_piece_index],
            original_board.available_pieces[min_piece_index]
        )
    print(board)
    print(pieces_score)
    print(*original_board.available_pieces)
    print()
    return boards_scores[hash(original_board)]


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
    parser.add_argument(
        "-i",
        "--interactive",
        help="Play your game and interact with the solver",
        action="store_true"
    )
    parser.add_argument(
        "-spi",
        "--solve-piece",
        help="Suggest a piece to give to the opponent",
        action="store_true"
    )
    parser.add_argument(
        "-spo",
        "--solve-position",
        help="Suggest where to put the piece you were given",
        action="store_true"
    )
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
