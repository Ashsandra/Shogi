import piece
import square


class Relay(piece.Piece):

    def __init__(self, lowerSide):
        self.origin = Relay
        self.lowerSide = lowerSide

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " r"
        else:
            return " R"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX(), start.getY()
        candidate = [(i, j+1), (i+1,j+1), (i-1, j-1),
                     (i+1, j-1), (i-1, j+1)]
        res = []
        for x, y in candidate:
            if 0 <= x <= 4 and 0 <= y <= 4 \
                    and (not board[x][y].getPiece() or board[x][y].getPiece().isLower() != start.getPiece().isLower()):
                res.append(board[x][y])
        return res

    def canMove(self, player, board, start, end):
        if not self.checkMoveBasics(start, end):
            return False
        startX = start.getX()
        startY = start.getY()
        endX = end.getX()
        endY = end.getY()
        xDif = abs(startX - endX)
        yDif = abs(startY - endY)
        if xDif + yDif != 2:
            if not (startX == endX and startY - endY == -1):
                return False
        if end.getPiece():
            player.setCapture(end.getPiece().origin)
        board[endX][endY].setPiece(start.getPiece())
        board[startX][startY].setPiece(None)
        return True