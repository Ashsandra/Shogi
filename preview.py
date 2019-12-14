import piece
import square


class Preview(piece.Piece):

    def __repr__(self):
        if self.lowerSize:
            return " p"
        else:
            return " P"

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
            player.setCapture(end.getPiece())
        board[endX][endY] = square.Square(start.getPiece(), endX, endY)
        return True

