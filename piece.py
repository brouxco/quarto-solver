class Piece(object):
    def __init__(self,
                 is_tall: bool,
                 is_dark: bool,
                 is_square: bool,
                 is_solid: bool):
        self.is_tall = is_tall
        self.is_dark = is_dark
        self.is_square = is_square
        self.is_solid = is_solid

    def __str__(self):
        return "{0}{1}{2}{3}".format(
                '1' if self.is_tall else '0',
                '1' if self.is_dark else '0',
                '1' if self.is_square else '0',
                '1' if self.is_solid else '0'
        )

    def __hash__(self):
        res = 0
        res += 1 if self.is_tall else 0
        res += 2 if self.is_dark else 0
        res += 4 if self.is_square else 0
        res += 8 if self.is_solid else 0
        return res

    def __eq__(self, other_piece):
        return self.__hash__() == other_piece.__hash__()

    def has_in_common_with(self, other_piece):
        return (self.is_tall == other_piece.is_tall
                or self.is_dark == other_piece.is_dark
                or self.is_square == other_piece.is_square
                or self.is_solid == other_piece.is_solid)


if __name__ == "__main__":
    pass
