import itertools
import piece


class Board(object):
    def __init__(self):
        self.available_pieces = []
        self.board = [[None for _ in range(4)] for _ in range(4)]

        for p in itertools.product([True, False], repeat=4):
            self.available_pieces.append(piece.Piece(*p))

    def is_row_losing(self, row):
        return (self.board[row][0]
                and self.board[row][1]
                and self.board[row][2]
                and self.board[row][3]
                and self.board[row][0].has_in_common_with(self.board[row][1])
                and self.board[row][1].has_in_common_with(self.board[row][2])
                and self.board[row][2].has_in_common_with(self.board[row][3]))

    def is_column_losing(self, col):
        return (self.board[0][col]
                and self.board[1][col]
                and self.board[2][col]
                and self.board[3][col]
                and self.board[0][col].has_in_common_with(self.board[1][col])
                and self.board[1][col].has_in_common_with(self.board[2][col])
                and self.board[2][col].has_in_common_with(self.board[3][col]))

    def is_diagonal_losing(self):
        return (self.board[0][0]
                and self.board[1][1]
                and self.board[2][2]
                and self.board[3][3]
                and self.board[0][0].has_in_common_with(self.board[1][1])
                and self.board[1][1].has_in_common_with(self.board[2][2])
                and self.board[2][2].has_in_common_with(self.board[3][3]))

    def is_reverse_diagonal_losing(self):
        return (self.board[0][3]
                and self.board[1][2]
                and self.board[2][1]
                and self.board[3][0]
                and self.board[0][3].has_in_common_with(self.board[1][2])
                and self.board[1][2].has_in_common_with(self.board[2][1])
                and self.board[2][1].has_in_common_with(self.board[3][0]))

    def is_move_allowed(self, x, y):
        return self.board[x][y] is None

    def is_move_losing(self):
        for i in range(4):
            if self.is_row_losing(i):
                return True
            if self.is_column_losing(i):
                return True
        return (self.is_diagonal_losing()
                or self.is_reverse_diagonal_losing())

    def allowed_moves(self):
        moves = []
        for x in range(4):
            for y in range(4):
                if self.is_move_allowed(x, y):
                    moves.append((x, y))
        return moves

    def move(self, x, y, piece):
        if not self.is_move_allowed(x, y):
            return False
        if piece not in self.available_pieces:
            return False
        self.board[x][y] = piece
        self.available_pieces.remove(piece)
        return True
