class Piece(object):
    def __init__(self,
                 is_tall: bool = True,
                 is_dark: bool = True,
                 is_square: bool = True,
                 is_solid: bool = True,
                 string: str = None):
        if string:
            self.is_tall = (string[0] == "1")
            self.is_dark = (string[1] == "1")
            self.is_square = (string[2] == "1")
            self.is_solid = (string[3] == "1")
        else:
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
        if not isinstance(other_piece, type(self)):
            return False
        return self.__hash__() == other_piece.__hash__()

    def has_in_common_with(self, *other_pieces):
        all_pieces_are_as_tall = True
        all_pieces_are_as_dark = True
        all_pieces_are_as_square = True
        all_pieces_are_as_solid = True

        for p in other_pieces:
            if not(self.is_tall == p.is_tall):
                all_pieces_are_as_tall = False
            if not(self.is_dark == p.is_dark):
                all_pieces_are_as_dark = False
            if not(self.is_square == p.is_square):
                all_pieces_are_as_square = False
            if not(self.is_solid == p.is_solid):
                all_pieces_are_as_solid = False

        return (all_pieces_are_as_tall
                or all_pieces_are_as_dark
                or all_pieces_are_as_square
                or all_pieces_are_as_solid)


if __name__ == "__main__":
    pass
