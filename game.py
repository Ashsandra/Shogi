import sys
from board import Board
from player import Player
from move import Move
import preview
import relay
import note
import governance
import promoted_governance
import promoted_preview
import promoted_notes
import promoted_relay


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

    def endGameByIllegalMove(self):
        print(self.currentPlayer.getOpponent() + " player wins. Illegal Move.")

    def endGameByCheckMate(self):
        print(repr(self.currentPlayer) + " player wins. Checkmate.")

    def endGameByStalemate(self):
        print ("Tie game. Too many moves.")

    def sendCheckMessage(self):
        print(self.currentPlayer.getOpponent() + " player is in check!")


def main():
    game = Game()
    mode = str(sys.argv[1])
    if mode == "-i":
        game.startInterativeMode()
        for i in range(201):
            if i == 200:
                game.endGameByStalemate()
            if not game.currentPlayer or game.currentPlayer == game.upperPlayer:
                game.currentPlayer = game.lowerPlayer
            else:
                game.currentPlayer = game.upperPlayer
            userInput = input(repr(game.currentPlayer) + "<")
            print(repr(game.currentPlayer) + "player " + "action: " + userInput)
            if not userInput:
                game.endGameByIllegalMove()
                break
            userInput = userInput.split()
            moveType = userInput[0]
            if moveType not in ["move", "drop"]:
                game.endGameByIllegalMove()
                break
            if moveType == "move":
                if not checkInputForMove(userInput):
                    game.endGameByIllegalMove()
                    break
                if not handlePlayerMove(game, userInput):
                    break


def checkInputForMove(userInput):
    if len(userInput) != 3 and len(userInput) != 4:
        return False
    for i in range(1,3):
        if len(userInput[i]) != 2 or userInput[i][0] not in "abcde" or userInput[i][1] not in "12345":
            return False
    if len(userInput) == 4 and userInput[3] != "promote":
        return False
    return True


def checkInputForDrop(userInput):
    if len(userInput) != 3:
        return False
    if len(userInput[2]) != 2 or userInput[2][0] not in "abcde" or userInput[i][1] not in "12345":
        return False
    return True


"""
A promotion is transferring one to its promoted version. It could not happen if piece could not be promoted, or if neither start nor end 
is in promotion zone. 
"""
def handlePromotion(game, userInput):
    starti, startj = game.transForm(userInput[1])
    endi, endj = game.transForm(userInput[2])
    end = game.board[endi][endj]
    targetRow = game.currentPlayer.getPromotionRow()
    if starti != targetRow and endi != targetRow:
        return False
    if not end.getPiece().canPromote:
        return False
    if isinstance(end.getPiece(), preview.Preview):
        end.setPiece(promoted_preview.PromotedPreview(end.getPiece().isLower()))
    elif isinstance(end.getPiece(), note.Note):
        end.setPiece(promoted_notes.PromotedNotes(end.getPiece().isLower()))
    elif isinstance(end.getPiece(), governance.Governance):
        end.setPiece(promoted_governance.PromotedGovernance(end.getPiece().isLower()))
    else:
        end.setPiece(promoted_relay.PromotedRelay(end.getPiece().isLower()))


def handleDrop(game,userInput):
    pass


def handlePlayerMove(game, userInput):
    starti, startj = game.transForm(userInput[1])
    endi, endj = game.transForm(userInput[2])
    start, end = game.board[starti][startj], game.board[endi][endj]
    if game.makeMove(start, end):
        movePreCheck = Move(getOpponent(game), game.board)
        if movePreCheck.isCheck(game.board):
            game.endGameByIllegalMove()
            return False
        else:
            if len(userInput) == 4:
                if not handlePromotion(game, userInput):
                    game.endGameByIllegalMove()
                    return False
            print(game.boardObject)
    else:
        game.endGameByIllegalMove()
        return False
    print()
    print("Captures UPPER:" + ' '.join([repr(c) for c in game.upperPlayer.captures]))
    print("Captures lower:" + ' '.join([repr(c) for c in game.lowerPlayer.captures]))
    print()
    move = Move(game.currentPlayer, game.board, start, end, None)
    if move.isCheck(game.board):
        game.sendCheckMessage()
        if move.isCheckMate(game.board):
            game.endGameByCheckMate()
            return False
        else:
            print("Available Moves:")
            candidate = move.generateCheckMoves(game.board)
            for c in candidate:
                print(c)
    return True

def getOpponent(game):
    return game.upperPlayer if game.currentPlayer == game.lowerPlayer else game.lowerPlayer


if __name__ == main():
    main()













