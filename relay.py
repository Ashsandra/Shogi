import piece
import square

class Relay(piece.Piece):

    def __init__(self):
        self.origin = Relay

    def __repr__(self):
        if self.lowerSide:
            return " r"
        else:
            return " R"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX, start.getY
        candidate = [(i, j+1), (i+1,j+1), (i-1, j-1),
                     (i+1, j-1), (i-1, j+1)]
        res = []
        for x, y in candidate:
            if 0 <= x <= 4 and 0 <= y <= 4 and board[x][y].getPiece().isLower() != start.getPiece().isLower():
                res.append((x,y))
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
        board[startX][startY] = square.Square(None, startX, startY)
        if end.getPiece():
            player.setCapture(end.getPiece().origin)
        board[endX][endY] = square.Square(start.getPiece(), endX, endY)
        return True