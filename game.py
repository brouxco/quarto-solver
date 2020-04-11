import copy
import random

# Contains the score, losing_piece and player
boards_scores = dict()


class Game(object):
    # return score, losing_piece and player
    @staticmethod
    def min_max(board, opponent):
        if hash(board) in boards_scores:
            return boards_scores[hash(board)]
        if board.is_move_losing():
            return 1 if opponent else -1, None, opponent
        if len(board.available_pieces) == 0:
            return 0, None, opponent
        original_board = copy.deepcopy(board)
        # may be interesting to use a dictionary instead
        pieces_score = [0 for _ in original_board.available_pieces]
        if not opponent:
            for i, p in enumerate(original_board.available_pieces):
                for move in original_board.allowed_moves():
                    board.place(*move, p)
                    score, _, enemy = Game.min_max(board, True)
                    if enemy:
                        pieces_score[i] -= score
                    else:
                        pieces_score[i] += score
                    board = copy.deepcopy(original_board)
            max_piece_index = pieces_score.index(max(pieces_score))
            boards_scores[hash(original_board)] = (
                pieces_score[max_piece_index],
                original_board.available_pieces[max_piece_index],
                opponent
            )
        else:
            for i, p in enumerate(original_board.available_pieces):
                for move in original_board.allowed_moves():
                    board.place(*move, p)
                    score, _, enemy = Game.min_max(board, False)
                    if enemy:
                        pieces_score[i] += score
                    else:
                        pieces_score[i] -= score
                    board = copy.deepcopy(original_board)
            min_piece_index = pieces_score.index(min(pieces_score))
            boards_scores[hash(original_board)] = (
                pieces_score[min_piece_index],
                original_board.available_pieces[min_piece_index],
                opponent
            )
        print(board)
        print(pieces_score)
        print(*original_board.available_pieces)
        print()
        return boards_scores[hash(original_board)]

    @staticmethod
    def monte_carlo(board, nb_iterations):
        original_board = copy.deepcopy(board)
        # may be interesting to use a dictionary
        pieces_score = [0 for _ in original_board.available_pieces]
        # would be cool to run it until the user presses Ctrl+C (SIGINT)
        for _ in range(nb_iterations):
            board = copy.deepcopy(original_board)

            opponent = False

            piece = random.choice(board.available_pieces)
            move = random.choice(board.allowed_moves())
            i = board.available_pieces.index(piece)

            board.place(*move, piece)

            while not board.is_move_losing() and len(board.available_pieces):
                p = random.choice(board.available_pieces)
                m = random.choice(board.allowed_moves())

                board.place(*m, p)

                opponent = not opponent

            if not board.is_move_losing():
                continue
            if opponent:
                pieces_score[i] += 1
            else:
                pieces_score[i] -= 1

        max_piece_index = pieces_score.index(max(pieces_score))

        return (
            pieces_score[max_piece_index],
            original_board.available_pieces[max_piece_index]
        )
