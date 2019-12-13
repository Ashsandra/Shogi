import piece


class Note(piece.Piece):

    def __repr__(self):
        if self.lowerSize:
            return " n"
        else:
            return " N"

    def canMove(self, board, start, end):
        pass