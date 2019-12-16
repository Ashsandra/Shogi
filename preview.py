import piece


class Preview(piece.Piece):

    def __init__(self, lowerSide):
        self.origin = Preview
        self.lowerSide = lowerSide
        self.canPromote = True

    def getCaptureRepr(self):
        if self.lowerSide:
            return "p"
        else:
            return "P"

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " p"
        else:
            return " P"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX(), start.getY()
        if self.lowerSide:
            if 0 <= i <= 4 and 0 <= j <= 3 \
                    and (not board[i][j+1].getPiece() or board[i][j+1].getPiece().isLower() != start.getPiece().isLower()):
                return [board[i-1][j]]
        else:
            if 0 <= i <= 4 and 1 <= j <= 4 \
                    and (not board[i][j - 1].getPiece() or board[i][j - 1].getPiece().isLower() != start.getPiece().isLower()):
                return [board[i+1][j]]
        return []

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

