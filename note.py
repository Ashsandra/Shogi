import piece
import square


class Note(piece.Piece):

    def __init__(self, lowerSide):
        self.origin = Note
        self.lowerSide = lowerSide

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " n"
        else:
            return " N"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX(), start.getY()
        res = []
        i += 1
        while i < 5:
            if not board[i][j].getPiece():
                res.append(board[i][j])
                i += 1
            else:
                if board[i][j].getPiece().isLower() != start.getPiece().isLower():
                    res.append(board[i][j])
                break
        i = start.getX()-1
        while i >= 0:
            if not board[i][j].getPiece():
                res.append(board[i][j])
                i -= 1
            else:
                if board[i][j].getPiece().isLower() != start.getPiece().isLower():
                    res.append(board[i][j])
                break
        j += 1
        while j < 5:
            if not board[i][j].getPiece():
                res.append(board[i][j])
                j += 1
            else:
                if board[i][j].getPiece().isLower() != start.getPiece().isLower():
                    res.append(board[i][j])
                break
        j = start.getY()-1
        while j >= 0:
            if not board[i][j].getPiece():
                res.append(board[i][j])
                j -= 1
            else:
                if board[i][j].getPiece().isLower() != start.getPiece().isLower():
                    res.append(board[i][j])
                break
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
        if end.getPiece():
            player.setCapture(end.getPiece().origin(not player.lowerSide))
        board[endX][endY].setPiece(start.getPiece())
        board[startX][startY].setPiece(None)
        return True
