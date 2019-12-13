import piece


class Governance(piece.Piece):

    def __repr__(self):
        if self.lowerSize:
            return " g"
        else:
            return " G"

    def canMove(self, board, start, end):
        pass