import piece
import square


class Shield(piece.Piece):

    def __init__(self, lowerSide):
        self.origin = Shield
        self.lowerSide = lowerSide

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " s"
        else:
            return " S"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX, start.getY
        candidate = [(i+1, j), (i-1,j), (i, j+1), (i, j-1), (i+1,j+1),
                      (i-1, j+1)]
        res = []
        for x, y in candidate:
            if 0 <= x <= 4 and 0 <= y <= 4 and board[x][y].getPiece().isLower() != start.getPiece().isLower():
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

        if xDif + yDif != 1:
            if not (xDif == 1 and yDif == 1) or (startY - endY == -1):
                return False
        board[startX][startY] = square.Square(None, startX, startY)
        if end.getPiece():
            player.setCapture(end.getPiece().origin)
        board[endX][endY] = square.Square(start.getPiece(), endX, endY)
        return True