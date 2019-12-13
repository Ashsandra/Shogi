import piece


class Preview(piece.Piece):

    def __repr__(self):
        if self.lowerSize:
            return " p"
        else:
            return " P"

    def canMove(self, board, start, end):
        pass