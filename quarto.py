import game
import piece
import board
import copy

boards_scores = dict()


# return score, losing_piece
def find_losing_piece(board, enemy):
    if hash(board) in boards_scores:
        return boards_scores[hash(board)]
    if board.is_move_losing():
        return 1, None
    if len(board.available_pieces) == 0:
        return 0, None
    # print()
    original_board = copy.deepcopy(board)
    pieces_score = [0 for _ in original_board.available_pieces]
    if not enemy:
        for i, p in enumerate(original_board.available_pieces):
            for move in original_board.allowed_moves():
                board.place(*move, p)
                score, _ = find_losing_piece(board, False)
                pieces_score[i] += score
                board = copy.deepcopy(original_board)
    else:
        for i, p in enumerate(original_board.available_pieces):
            for move in original_board.allowed_moves():
                board.place(*move, p)
                score, _ = find_losing_piece(board, True)
                pieces_score[i] += score
                board = copy.deepcopy(original_board)
    print(board)
    print(pieces_score)
    print(*original_board.available_pieces)
    print()
    min_piece_score = 2**64
    min_piece = None
    for i, score in enumerate(pieces_score):
        if score == 0:
            continue
        if score < min_piece_score:
            min_piece_score = score
            min_piece = original_board.available_pieces[i]

    if min_piece is None:
        min_piece_score = 0
        min_piece = original_board.available_pieces[0]

    boards_scores[hash(original_board)] = (
        min_piece_score,
        min_piece
    )
    return boards_scores[hash(original_board)]


def main():
    b = board.Board()
    # b.available_pieces = [piece.Piece(True, True, True, False),
    #                       piece.Piece(True, True, True, True),
    #                       piece.Piece(True, True, False, True),
    #                       piece.Piece(True, True, False, False)]
    # print(b.allowed_moves())
    # print(*b.available_pieces)
    b.place(0, 0, piece.Piece(True, True, True, True))
    b.place(0, 1, piece.Piece(True, True, True, False))
    b.place(0, 2, piece.Piece(True, True, False, True))
    b.place(0, 3, piece.Piece(False, False, True, False))
    b.place(1, 0, piece.Piece(True, True, False, False))
    b.place(1, 1, piece.Piece(True, False, True, True))
    b.place(1, 2, piece.Piece(True, False, True, False))
    b.place(1, 3, piece.Piece(False, True, False, True))
    b.place(2, 0, piece.Piece(True, False, False, False))
    # b.place(2, 1, piece.Piece(False, False, True, True))
    # b.place(2, 2, piece.Piece(True, False, False, True))
    # b.place(2, 3, piece.Piece(False, True, True, True))
    # b.place(3, 0, piece.Piece(False, True, False, False))
    print(*find_losing_piece(copy.deepcopy(b), False))
    print(len(boards_scores))
    # print()
    # for bo in sorted(boards_scores, key=str):
    #     print(bo)
    # b.place(0, 0, piece.Piece(True, True, True, True))
    # boards_scores.add(b)
    # boards_scores.add(copy.deepcopy(b))
    # print(boards_scores)
    g = game.Game()
    g.find_losing_piece()


if __name__ == "__main__":
    main()
