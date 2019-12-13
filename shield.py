import piece


class Shield(piece.Piece):

    def __repr__(self):
        if self.lowerSize:
            return " s"
        else:
            return " S"

    def canMove(self, board, start, end):
        pass