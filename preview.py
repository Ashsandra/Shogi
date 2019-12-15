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
        i, j = start.getX(), start.getY()
        if 0 <= i <= 4 and 0 <= j <= 3 \
                and (not board[i][j+1].getPiece() or board[i][j+1].getPiece().isLower() != start.getPiece().isLower()):
            return [board[i][j+1]]
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
        if end.getPiece():
            player.setCapture(end.getPiece().origin(not player.lowerSide))
        board[endX][endY].setPiece(start.getPiece())
        board[startX][startY].setPiece(None)
        return True

