import piece


class Preview(piece.Piece):
    """
    Class that represents a preview piece.
    """
    def __init__(self, lowerSide):
        self.origin = Preview
        self.lowerSide = lowerSide
        self.canPromote = True
        self.ID = id(Preview)

    def getCaptureRepr(self):
        """
        :return: representation after being captured
        """
        if self.lowerSide:
            return "p"
        else:
            return "P"

    def __repr__(self):
        if self.lowerSide is None:
            return "__"
        if self.lowerSide:
            return " p"
        else:
            return " P"

    def generatePossibleMoves(self, board, start):
        """
        :param board: the chess board
        :param start: the starting position
        :return: all valid moves of drive starting from index position.
        """
        i, j = start.getX(), start.getY()
        if self.lowerSide:
            if 1 <= i <= 4 and 0 <= j <= 4 \
                    and (not board[i-1][j].getPiece() or board[i-1][j].getPiece().isLower() != start.getPiece().isLower()):
                return [board[i-1][j]]
        else:
            if 0 <= i <= 3 and 0 <= j <= 4 \
                    and (not board[i+1][j].getPiece() or board[i+1][j].getPiece().isLower() != start.getPiece().isLower()):
                return [board[i+1][j]]
        return []

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

