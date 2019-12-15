import piece
import square


class Preview(piece.Piece):

    def __init__(self, lowerSide):
        self.origin = Preview
        self.lowerSide = lowerSide

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " p"
        else:
            return " P"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX, start.getY
        if 0 <= i <= 4 and 0 <= j <= 3:
            return [board[x][y]]
        else:
            return []

    def canMove(self, player, board, start, end):
        if not self.checkMoveBasics(start, end):
            return False
        startX = start.getX()
        startY = start.getY()
        endX = end.getX()
        endY = end.getY()
        if startX != endX:
            return False
        if not endY - startY == 1:
            return False
        board[startX][startY] = square.Square(None, startX, startY)
        if end.getPiece():
            player.setCapture(end.getPiece().origin)
        board[endX][endY] = square.Square(start.getPiece(), endX, endY)
        return True

