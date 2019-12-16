import piece


class Governance(piece.Piece):
    """
    Class that represents a governance chess piece.
    """

    def __init__(self, lowerSide):
        self.origin = Governance
        self.canPromote = True
        self.lowerSide = lowerSide
        self.ID = id(Governance)

    def getCaptureRepr(self):
        """
        :return: representation after being captured
        """
        if self.lowerSide:
            return "g"
        else:
            return "G"

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " g"
        else:
            return " G"

    def generatePossibleMoves(self, board, start):
        """
        :param board: the chess board
        :param start: the starting position
        :return: all valid moves of drive starting from index position.
        """
        i, j = start.getX(), start.getY()
        res = []
        # checking the upper right diagonal
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
        # checking the down right diagonal
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
        # checking the upper left diagonal
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
        # checking the down left diagonal
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

    def canMove(self, player, board, start, end, changeCapture = True):
        """
        :param player: the current player
        :param board: the chess board
         :param start: the starting position
        :param end: the ending position
        :param changeCapture: boolean indicating whether the captureList needs to be changed
        :return: whether the player could move from start to end in the given board
        """
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