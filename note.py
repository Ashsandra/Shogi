import piece


class Note(piece.Piece):
    """
    Class that represents a note chess piece.
    """

    def __init__(self, lowerSide):
        self.ID = id(Note)
        self.origin = Note
        self.lowerSide = lowerSide
        self.canPromote = True

    def getCaptureRepr(self):
        """
        :return: representation after being captured
        """
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
        """
        :param board: the chess board
        :param start: the starting position
        :return: all valid moves of drive starting from index position.
        """
        i, j = start.getX(), start.getY()
        res = []
        i += 1
        # check the four directions notes could go one by one
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
