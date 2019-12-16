import piece


class Note(piece.Piece):

    def __init__(self, lowerSide):
        self.ID = id(Note)
        self.origin = Note
        self.lowerSide = lowerSide
        self.canPromote = True

    def getCaptureRepr(self):
        if self.lowerSide:
            return "n"
        else:
            return "N"

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
        i = start.getX()
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
