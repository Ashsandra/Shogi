import piece


class Relay(piece.Piece):

    def __repr__(self):
        if self.lowerSize:
            return " r"
        else:
            return " R"

    def canMove(self, board, start, end):
        pass