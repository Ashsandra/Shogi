import piece


class Governance(piece.Piece):

    def __init__(self, lowerSide):
        self.origin = Governance
        self.canPromote = True
        self.lowerSide = lowerSide
        self.ID = id(Governance)

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " g"
        else:
            return " G"

    def generatePossibleMoves(self, board, start):
        i, j = start.getX(), start.getY()
        res = []
        i += 1
        j += 1
        while i < 5 and j < 5:
            if not board[i][j].getPiece():
                res.append(board[i][j])
                i += 1
                j += 1
            else:
                if board[i][j].getPiece().isLower() != start.getPiece().isLower():
                    res.append(board[i][j])
                break
        i = start.getX() - 1
        j = start.getY() - 1
        while i >= 0 and j >= 0:
            if not board[i][j].getPiece():
                res.append(board[i][j])
                i -= 1
                j -= 1
            else:
                if board[i][j].getPiece().isLower() != start.getPiece().isLower():
                    res.append(board[i][j])
                break
        i = start.getX() + 1
        j = start.getY() - 1
        while i < 5 and j >= 0:
            if not board[i][j].getPiece():
                res.append(board[i][j])
                j -= 1
                i += 1
            else:
                if board[i][j].getPiece().isLower() != start.getPiece().isLower():
                    res.append(board[i][j])
                break
        i = start.getX() - 1
        j = start.getY() + 1
        while i >= 0 and j < 5:
            if not board[i][j].getPiece():
                res.append(board[i][j])
                j += 1
                i -= 1
            else:
                if board[i][j].getPiece().isLower() != start.getPiece().isLower():
                    res.append(board[i][j])
                break
        return res

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

    def canMove(self, player, board, start, end, changeCapture = True):
        if not self.checkMoveBasics(start, end):
            return False
        allMoves = self.generatePossibleMoves(board, start)
        if end not in allMoves:
            return False
        if end.getPiece():
            if changeCapture:
                player.setCapture(end.getPiece().origin(player.lowerSide))
        end.setPiece(start.getPiece())
        start.setPiece(None)
        return True