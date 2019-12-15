class Move:
    def __init__(self, player, board, start, end, drop = None):
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

    def getOpponentKing(self):
        if self.player.isLowerSide():
            target = " D"
        else:
            target = " d"

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if repr(self.board[i][j].getPiece()) == target:
                    return i,j

    def isCheck(self):
        pass

    def isCheckMate(self):
        pass

    def generateCheckMoves(self):
        pass

    def canDrop(self):
        if not self.drop:
            return False
        if self.drop not in self.captures:
            return False
        if self.drop in

    def canMove(self):
        return self.piece.canMove(self.player, self.board, self.start, self.end )




