import piece


class Drive(piece.Piece):

    def __repr__(self):
        if self.lowerSize:
            return " d"
        else:
            return " D"

    def canMove(self, board, start, end):
        pass

