import piece
import square

class Governance(piece.Piece):

    def __init__(self):
        self.origin = Governance

    def __repr__(self):
        if self.lowerSize:
            return " g"
        else:
            return " G"

    def checkDecreaseDiagonal(self, board, low, high):
        lowX = low.getX()
        highX = high.getX()-1
        highY = high.getY()-1
        while lowX != highX:
            if board[highX][highY].getPiece():
                return False
            highX += 1
            highY -= 1
        return True

    def checkIncreaseDiagonal(self, board, low, high):
        lowX = low.getX() + 1
        lowY = low.getY() + 1
        highX = high.getX()
        while lowX != highX:
            if board[lowX][lowY].getPiece():
                return False
            lowX += 1
            lowY += 1
        return True

    def canMove(self, player, board, start, end):
        if not self.checkMoveBasics(start, end):
            return False
        startX = start.getX()
        startY = start.getY()
        endX = end.getX()
        endY = end.getY()
        if not (startX + startY == endX + endY or startX - endY == endX - endY):
            return False
        # decrease diagonal
        if startX + startY == endX + endY:
            if startY < endY:
                flag = self.checkDecreaseDiagonal(start, end)
            else:
                flag = self.self.checkDecreaseDiagonal(end, start)
        else:
            if startX < endX:
                flag = self.checkDecreaseDiagonal(start, end)
            else:
                flag = self.self.checkDecreaseDiagonal(end, start)
        if not flag:
            return False
        board[startX][startY] = square.Square(None, startX, startY)
        if end.getPiece():
            player.setCapture(end.getPiece().origin)
        board[endX][endY] = square.Square(start.getPiece(), endX, endY)
        return True