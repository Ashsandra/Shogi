import sys
from board import Board
from player import Player
from move import Move


class Game:

    def __init__(self):
        self.boardObject = Board()
        self.board = self.boardObject.getBoard()
        self.upperPlayer = Player(False)
        self.lowerPlayer = Player(True)
        self.currentPlayer = None
        self.allStatus = ["upperWin", "lowerWin", "stalemate", "active"]
        self.status = None


    def startInterativeMode(self):
        print(self.boardObject)
        print()
        print("Captures UPPER:" + ' '.join(self.upperPlayer.captures))
        print("Captures lower:" + ' '.join(self.lowerPlayer.captures))
        print()

    def startFileGameMode(self):
        pass

    def makeMove(self, start, end):
        move = Move(self.currentPlayer, self.board, start, end, None)
        return move.canMove(self.currentPlayer, self.board, start, end)

    def makeDrop(self, board, piece, end, captures):
        move = Move(self.currentPlayer, self.board, start, end, None)
        return move.canDrop(board, piece, end, captures)

    def transForm(self, repr):
        i = 5 - int(repr[1])
        j = ord(repr[0]) - 97
        return i, j

def main():
    game = Game()
    mode = str(sys.argv[1])
    if mode == "-i":
        game.startInterativeMode()
        for i in range(200):
            if not game.currentPlayer or game.currentPlayer == game.upperPlayer:
                game.currentPlayer = game.lowerPlayer
            else:
                game.currentPlayer = game.upperPlayer
            user_input = input(repr(game.currentPlayer) + "<")
            print(repr(game.currentPlayer) + "player " + "action: " + user_input)
            user_input = user_input.split()
            moveType = user_input[0]
            if moveType == "move":
                starti, startj = game.transForm(user_input[1])
                endi, endj = game.transForm(user_input[2])
                start, end = game.board[starti][startj], game.board[endi][endj]
                if game.makeMove(start, end):
                    movePreCheck = Move(getOpponent(game), game.board)
                    if movePreCheck.isCheck(game.board):
                        print(repr(getOpponent(game)) + " player wins. Illegal Move")
                        break
                    else:
                        print(game.boardObject)
                else:
                    print(game.currentPlayer.getOpponent() + " player wins. Illegal Move")
                    break
                print()
                print("Captures UPPER:" + ' '.join([repr(c) for c in game.upperPlayer.captures]))
                print("Captures lower:" + ' '.join([repr(c) for c in game.lowerPlayer.captures]))
                print()
                move = Move(game.currentPlayer, game.board, start, end, None)
                if move.isCheck(game.board):
                    print(game.currentPlayer.getOpponent() + " player is in check!")
                    if move.isCheckMate(game.board):
                        print(repr(game.currentPlayer) + " player wins. Checkmate")
                        break
                    else:
                        print("Available Moves:")
                        candidate = move.generateCheckMoves(game.board)
                        for c in candidate:
                            print(c)


def getOpponent(game):
    return game.upperPlayer if game.currentPlayer == game.lowerPlayer else game.lowerPlayer


if __name__ == main():
    main()













