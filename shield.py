import piece
import square

class Shield(piece.Piece):

    def __repr__(self):
        if self.lowerSize:
            return " s"
        else:
            return " S"

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
            player.setCapture(end.getPiece())
        board[endX][endY] = square.Square(start.getPiece(), endX, endY)
        return True