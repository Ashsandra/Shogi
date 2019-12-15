import piece
import square


class Drive(piece.Piece):

    def __init__(self, lowerSide):
        self.origin = Drive
        self.lowerSide = lowerSide

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
        startX = start.getX()
        startY = start.getY()
        endX = end.getX()
        endY = end.getY()
        xDif = abs(startX - endX)
        yDif = abs(startY - endY)
        if xDif + yDif != 1:
            if not (xDif == 1 and yDif == 1):
                return False
        if end.getPiece():
            if changeCapture:
                player.setCapture(end.getPiece().origin(not player.lowerSide))
        board[endX][endY].setPiece(start.getPiece())
        board[startX][startY].setPiece(None)

        return True


