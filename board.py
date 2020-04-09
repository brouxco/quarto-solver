import itertools
import piece


class Board(object):
    def __init__(self):
        self.available_pieces = []
        self.board = [[None for _ in range(4)] for _ in range(4)]

        for p in itertools.product([True, False], repeat=4):
            self.available_pieces.append(piece.Piece(*p))

    def __str__(self):
        res = ''
        for row in range(4):
            for col in range(4):
                res += str(self.board[row][col]) + ' '
            res += '\n'
        return res

    def __hash__(self):
        # We should have the same hash for identical boards
        # even rotated and/or symmetrical boards
        identical_boards = set()
        for _ in range(4):
            s = str(self)

            self.__mirror_vertical()
            s_m_v = str(self)
            self.__mirror_vertical()

            self.__mirror_horizontal()
            s_m_h = str(self)
            self.__mirror_horizontal()

            self.__mirror_diagonal()
            s_m_d = str(self)
            self.__mirror_diagonal()

            self.__mirror_reverse_diagonal()
            s_m_r_d = str(self)
            self.__mirror_reverse_diagonal()

            self.__rotate_90()

            identical_boards.add(s)
            identical_boards.add(s_m_v)
            identical_boards.add(s_m_h)
            identical_boards.add(s_m_d)
            identical_boards.add(s_m_r_d)
        res = ''
        for board in sorted(identical_boards, key=str):
            res += str(board)
        return res.__hash__()

    def __eq__(self, other_board):
        if not isinstance(other_board, type(self)):
            return False
        return self.__hash__() == other_board.__hash__()

    def __rotate_90(self):
        self.board = [list(reversed(x)) for x in zip(*self.board)]

    def __mirror_vertical(self):
        self.board = [list(reversed(x)) for x in self.board]

    def __mirror_horizontal(self):
        self.board = [list(x) for x in reversed(self.board)]

    def __mirror_diagonal(self):
        self.board = [list(x) for x in zip(*self.board)]

    def __mirror_reverse_diagonal(self):
        self.__mirror_vertical()
        self.__mirror_diagonal()
        self.__mirror_vertical()

    def is_row_losing(self, row):
        return (self.board[row][0]
                and self.board[row][1]
                and self.board[row][2]
                and self.board[row][3]
                and self.board[row][0].has_in_common_with(
                    self.board[row][1],
                    self.board[row][2],
                    self.board[row][3]))

    def is_column_losing(self, col):
        return (self.board[0][col]
                and self.board[1][col]
                and self.board[2][col]
                and self.board[3][col]
                and self.board[0][col].has_in_common_with(
                    self.board[1][col],
                    self.board[2][col],
                    self.board[3][col]))

    def is_diagonal_losing(self):
        return (self.board[0][0]
                and self.board[1][1]
                and self.board[2][2]
                and self.board[3][3]
                and self.board[0][0].has_in_common_with(
                    self.board[1][1],
                    self.board[2][2],
                    self.board[3][3]))

    def is_reverse_diagonal_losing(self):
        return (self.board[0][3]
                and self.board[1][2]
                and self.board[2][1]
                and self.board[3][0]
                and self.board[0][3].has_in_common_with(
                    self.board[1][2],
                    self.board[2][1],
                    self.board[3][0]))

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

    def place(self, x, y, piece):
        if not self.is_move_allowed(x, y):
            return False
        if piece not in self.available_pieces:
            return False
        self.board[x][y] = piece
        self.available_pieces.remove(piece)
        return True
