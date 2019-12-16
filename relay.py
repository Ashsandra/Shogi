import piece


class Relay(piece.Piece):

    def __init__(self, lowerSide):
        self.origin = Relay
        self.lowerSide = lowerSide
        self.canPromote = True

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " r"
        else:
            return " R"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX(), start.getY()
        if self.lowerSide:
            candidate = [(i-1, j+1), (i-1,j), (i-1, j-1),
                     (i+1, j-1), (i+1, j+1)]
        else:
            candidate = [(i+1, j+1), (i+1,j), (i+1, j-1),
                     (i-1, j-1), (i-1, j+1)]

        res = []
        for x, y in candidate:
            if 0 <= x <= 4 and 0 <= y <= 4 \
                    and (not board[x][y].getPiece() or board[x][y].getPiece().isLower() != start.getPiece().isLower()):
                res.append(board[x][y])
        return res

    def canMove(self, player, board, start, end, changeCapture = True):
        if not self.checkMoveBasics(start, end):
            return False
        allMoves = self.generatePossibleMoves(board, start)
        if end not in allMoves:
            return False
        if end.getPiece():
            if changeCapture:
                player.setCapture(end.getPiece().origin(player.lowerSide))
        end.setPiece(start.getPiece())
        start.setPiece(None)
        return True