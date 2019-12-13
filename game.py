import board


class Game:

    def __init__(self):
        self.board = None
        self.allStatus = ["upperWin", "lowerWin", "stalemate", "active"]
        self.status = None
        self.playes = []
        self.currentPlayer = None

    def startGame(self, player1, player2):
        self.players[0] = player1
        self.players[1] = player2
        self.board = self.board.Board.board()
        self.status = "active"
        if player1.isLowerSide:
            self.currentPlayer = player1
        else:
            self.currentPlayer = player2

    def isEnd(self):
        return self.status != "active"

    def setStatus(self,status):
        self.status = status

    def getStatus(self):
        return self.status

    def makeMove(self):
        pass











