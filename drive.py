import piece



class Drive(piece.Piece):

    def __init__(self, lowerSide):
        self.ID = id(Drive)
        self.origin = Drive
        self.lowerSide = lowerSide
        self.canPromote = False


    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " d"
        else:
            return " D"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX(), start.getY()
        candidate = [(i+1, j), (i-1,j), (i, j+1), (i, j-1), (i+1,j+1), (i-1, j-1),
                (i+1, j-1), (i-1, j+1)]

        res = []
        for x, y in candidate:
            if 0 <= x <= 4 and 0 <= y <= 4 and \
                    (not board[x][y].getPiece() or board[x][y].getPiece().isLower() != start.getPiece().isLower()):
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


