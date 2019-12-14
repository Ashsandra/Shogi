import piece
import square


class Note(piece.Piece):

    def __init__(self):
        self.origin = Note

    def __repr__(self):
        if self.lowerSize:
            return " n"
        else:
            return " N"

    def canMove(self, player, board, start, end):
        if not self.checkMoveBasics(start, end):
            return False
        startX = start.getX()
        startY = start.getY()
        endX = end.getX()
        endY = end.getY()
        xDif = abs(startX - endX)
        yDif = abs(startY - endY)
        if not xDif and not yDif:
            return False
        if not xDif:
            for j in range(startY+1, endY):
                if board[startX][j].getPiece():
                    return False
        elif not yDif:
            for i in range(startX+1, endX):
                if board[i][startY].getPiece():
                    return False
        else:
            return False
        board[startX][startY] = square.Square(None, startX, startY)
        if end.getPiece():
            player.setCapture(end.getPiece().origin)
        board[endX][endY] = square.Square(start.getPiece(), endX, endY)
        return True
