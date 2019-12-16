import copy


class Move:
    """
    class that defines a series of checks for chess moves necessary for
    checking the validity of different chess moves.
    """
    def __init__(self, player, opponent, board, start=None, end=None, drop=None):
        self.opponent = opponent
        self.player = player
        self.board = board
        self.start = start
        self.end = end
        self.drop = drop
        self.captures = player.captures
        if not self.start:
            self.piece = drop
        else:
            self.piece = start.getPiece()

    def getOpponentKing(self, board):
        """
        method that gets the opponent's king position
        :param board: chess board
        :return: opponent's king position
        """
        if self.player.isLowerSide():
            target = " D"
        else:
            target = " d"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if repr(board[i][j].getPiece()) == target:
                    return board[i][j]

    def getKing(self, board):
        """
        method that gets the player's king position
         :param board: chess board
        :return: opponent's king position
        """
        if self.player.isLowerSide():
            target = " d"
        else:
            target = " D"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if repr(board[i][j].getPiece()) == target:
                    return board[i][j]

    def getAllLowerPieces(self, board):
        """
        :param board: chess board
        :return: all active pieces belonging to lower player.
        """
        res = []
        if self.player.isLowerSide():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if repr(board[i][j].getPiece()).islower():
                        res.append(board[i][j])
        return res

    def getAllUpperPieces(self, board):
        """
        :param board: chess board
        :return: all active pieces belonging to upper player.
        """
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if repr(board[i][j].getPiece()).isupper():
                    res.append(board[i][j])
        return res

    def isCheck(self, board):
        """
        :param board: chess board
        :return: True if opponent is in check by player given chess board, else False
        """
        kingPosition = self.getOpponentKing(board)
        if self.player.isLowerSide():
            allPieces = self.getAllLowerPieces(board)
        else:
            allPieces = self.getAllUpperPieces(board)
        for p in allPieces:
            candidate = p.getPiece().generatePossibleMoves(board, p)
            if kingPosition in candidate:
                return True
        return False

    def isCheckOppoSite(self, board):
        """
        :param board: chess board
        :return: True if player is in check by opponent given chess board, else False
        """
        kingPosition = self.getKing(board)
        if not self.player.isLowerSide():
            allPieces = self.getAllLowerPieces(board)
        else:
            allPieces = self.getAllUpperPieces(board)
        for p in allPieces:
            candidate = p.getPiece().generatePossibleMoves(board, p)
            if kingPosition in candidate:
                return True
        return False

    def isCheckMate(self, board):
        """
        :param board: chess board
        :return: True if opponent is in checkmate by player given chess board, else False
        """
        return False if self.generateCheckMoves(board) else True

    def generateCheckMoves(self, board):
        """
        Given the player's opponent is in check, generate all possible moves to "uncheck".
        :param board: the chess board
        :return: A list of possible moves that could be performed by the opponent.
        """
        res = []
        # possible moves for captured pieces
        for capture in self.opponent.captures:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if not board[i][j].getPiece():
                        newboard = self.canDrop(copy.deepcopy(self.board), capture, board[i][j])
                        if not newboard:
                            continue
                        if not self.isCheck(newboard):
                            res.append("drop" + " ".join([repr(capture).lower(), repr(board[i][j])]))
        # possible moves for active pieces
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].getPiece() and board[i][j].getPiece().isLower() != self.player.isLowerSide():
                    start, startPiece = board[i][j], board[i][j].getPiece()
                    endCandidate = startPiece.generatePossibleMoves(self.board, start)
                    for end in endCandidate:
                        newboard = copy.deepcopy(self.board)
                        newboard[end.getX()][end.getY()].setPiece(startPiece)
                        newboard[start.getX()][start.getY()].setPiece(None)
                        if not self.isCheck(newboard):
                            res.append("move " + " ".join([repr(start), repr(end)]))
        return sorted(res)

    def canDrop(self, board, piece, end):
        """
        :param board: the chess board
        :param piece: the piece to be dropped
        :param end: the ending position
        :return: True if piece could be dropped else False
        """
        pieceName = repr(piece)
        if pieceName == "p":
            if end.getX() == self.player.getPromotionRow():
                return False
            tempBoard = copy.deepcopy(board)
            if self.isCheck(tempBoard):
                return False
            if not self.player.isLowerSide():
                target = " P"
            else:
                target = " p"
            for i in range(len(board)):
                if board[i][end.getY()].getPiece():
                    if target == repr(self.board[i][end.getY()].getPiece()):
                        return False
        board[end.getX()][end.getY()].setPiece(piece)
        return board

    def canMove(self, player, board, start, end, capture = True):
        """
        :param player: the current player
        :param board: the chess board
        :param start: the starting position
        :param end: the ending position
        :param capture: boolean indicating whether to change the list of captures.
        :return:
        """
        if not start.getPiece():
            return False
        if start.getPiece().isLower() != player.isLowerSide():
            return False
        return start.getPiece().canMove(player, board, start, end, capture)




