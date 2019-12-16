import sys
from board import Board
from player import Player
from move import Move
import copy
import preview
import relay
import note
import governance
import shield
import promoted_governance
import promoted_preview
import promoted_notes
import promoted_relay
import drive
import utils


class Game:
    """
    class that represents the Game object used to run the game.
    """

    def __init__(self):
        self.boardObject = Board()  # an boardObject used to print the board representation to output
        self.board = self.boardObject.getBoard()
        self.upperPlayer = Player(False)
        self.lowerPlayer = Player(True)
        self.currentPlayer = None
        # a dict mapping each type of piece's string repr to there actual class type
        self.repr2Piece = {"g": governance.Governance, "n": note.Note, "r": relay. Relay, "s": shield.Shield,
                           "p": preview.Preview, "G": governance.Governance, "N": note.Note, "R": relay. Relay,
                           "S": shield.Shield,
                           "P": preview.Preview,
                           "d": drive.Drive, "D": drive.Drive,
                           "+G": promoted_governance.PromotedGovernance, "+g": promoted_governance.PromotedGovernance,
                           "+N": promoted_notes.PromotedNotes, "+n": promoted_notes.PromotedNotes,
                           "+p": promoted_preview.PromotedPreview, "+P": promoted_preview. PromotedPreview,
                           "+r": promoted_relay.PromotedRelay, "+R": promoted_relay.PromotedRelay}

    def startInterativeMode(self):
        """
        an default initialization for interative mode.
        :return: None
        """
        print(self.boardObject)
        print()
        print("Captures UPPER:" + ' '.join(self.upperPlayer.captures))
        print("Captures lower:" + ' '.join(self.lowerPlayer.captures))
        print()

    def startFileGameMode(self, filePath):
        """
        an initialization for file mode based on the file content.
        :param filePath:
        :return: the list containing all the moves specified by the file.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j].setPiece(None)
        d = utils.parseTestCase(filePath)
        moveList = d["moves"]
        boardUpdate = d["initialPieces"]
        for dict in boardUpdate:
            p = list(dict.keys())[0]
            i = list(dict.keys())[1]
            if dict[p][-1].isupper():
                piece = self.repr2Piece[dict[p]](False)
            else:
                 piece = self.repr2Piece[dict[p]](True)
            i, j = self.transForm(dict[i])
            self.board[i][j].setPiece(piece)
        self.upperPlayer.captures = [self.repr2Piece[p](False) for p in d["upperCaptures"]]
        self.lowerPlayer.captures = [self.repr2Piece[p](True) for p in d["lowerCaptures"]]
        return moveList

    def makeMove(self, start, end):
        """
        :param start: start position in board
        :param end: end position in board
        :return: True if move coudle be made else False
        """
        move = Move(self.currentPlayer, self.board, start, end, None)
        return move.canMove(self.currentPlayer, self.board, start, end)

    def makeDrop(self, piece, end):
        """
        :param start: start position in board
        :param end: end position in board
        :return: True if move coudle be made else False
        """
        move = Move(self.currentPlayer, self.board, None, end, piece)
        return move.canMove(self.board, piece, end, self.currentPlayer.captures)

    def transForm(self, repr):
        """
        :param repr: string repr of type similar to "a5"
        :return: tuple (i,j) representing it's position in matrix
        """
        i = 5 - int(repr[1])
        j = ord(repr[0]) - 97
        return i, j

    def endGameByIllegalMove(self):
        """
        An end game message caused by player's illegal move.
        :return: None
        """
        print(self.currentPlayer.getOpponent() + " player wins.  Illegal move.")

    def endGameByCheckMate(self):
        """
        An end game message caused by checkmate.
        :return: None
        """
        print(repr(self.currentPlayer) + " player wins.  Checkmate.")

    def endGameByStalemate(self):
        """
        An end game message caused by making too many moves.
        :return: None
        """
        print ("Tie game.  Too many moves.")

    def sendCheckMessage(self):
        """
        An in game message caused by the current board being in check.
        :return: None
        """
        print(self.currentPlayer.getOpponent() + " player is in check!")
        return ""

    def getCaptureInfo(self):
        """
        An in game message indicating the captures of the two players.
        :return: None
        """
        print("Captures UPPER:" + ' '.join([c.getCaptureRepr() for c in self.upperPlayer.captures]))
        print("Captures lower:" + ' '.join([c.getCaptureRepr() for c in self.lowerPlayer.captures]))
        return ""

    def getOpponent(self):
        """
        :return: the opponent of the current player.
        """
        return self.upperPlayer if self.currentPlayer == self.lowerPlayer else self.lowerPlayer


def main():
    game = Game()
    # read system input
    mode = str(sys.argv[1])
    if mode == "-i":
        game.startInterativeMode()
        for i in range(401):
            # at most 400 moves could be made
            if i == 400:
                game.endGameByStalemate()
            # set game player
            if not game.currentPlayer or game.currentPlayer == game.upperPlayer:
                game.currentPlayer = game.lowerPlayer
            else:
                game.currentPlayer = game.upperPlayer
            # prompt for user input
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
            else: # must be "drop"
                if not checkInputForDrop(userInput):
                    game.endGameByIllegalMove()
                    break
                if not handleDrop(game, userInput):
                    break
    else:
        filePath = sys.argv[2]
        moveList = game.startFileGameMode(filePath)
        gameTurn = 0
        for userInput in moveList:
            # set current player
            if not game.currentPlayer or game.currentPlayer == game.upperPlayer:
                game.currentPlayer = game.lowerPlayer
            else:
                game.currentPlayer = game.upperPlayer
            if not userInput:
                game.endGameByIllegalMove()
                break
            userInput = userInput.split()
            moveType = userInput[0]
            if moveType not in ["move", "drop"]:
                game.endGameByIllegalMove()
                break
            if moveType == "move":
                # first, check if the move is illegal, if so, print the board state and exit
                if not checkFileMoveIllegal(game, userInput):
                    print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                    print(game.boardObject)
                    print(game.getCaptureInfo())
                    game.endGameByIllegalMove()
                    break
                # then, check if the move causes checkmate, if so, print the board state and exit
                if checkFileMoveCheck(game, userInput):
                    if checkFileMoveCheckMate(game, userInput):
                        print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                        print(game.boardObject)
                        print(game.getCaptureInfo())
                        game.endGameByCheckMate()
                        break
                    else:
                        # if this is the last move, we also need to print the board state
                        if gameTurn == len(moveList) - 1:
                            print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                            print(game.boardObject)
                            print(game.getCaptureInfo())
                            print(game.currentPlayer.getOpponent() + " player is in check!")
                            print("Available moves:")
                            candidate = getFileMoveAvailMoves(game, userInput)
                            for c in candidate:
                                print(c)
                            print(game.currentPlayer.getOpponent() + ">")

                else:
                    if gameTurn == 399: # move limit has been reached, end game by stalemate
                        print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                        print(game.boardObject)
                        print(game.getCaptureInfo())
                        game.endGameByStalemate()
                        break
                    # we need to print the board state if this is the last move
                    if gameTurn == len(moveList) - 1:
                        print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                        print(game.boardObject)
                        print(game.getCaptureInfo())
                        print(game.currentPlayer.getOpponent() + ">")
            else:
                # we follow very similar logic for drop
                if not checkFileDropIllegal(game, userInput):
                    print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                    print(game.boardObject)
                    print(game.getCaptureInfo())
                    game.endGameByIllegalMove()
                    break
                if checkFileDropCheck(game, userInput):
                    if checkFileDropCheckMate(game, userInput):
                        print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                        print(game.boardObject)
                        print(game.getCaptureInfo())
                        game.endGameByCheckMate()
                        break
                    else:
                        if gameTurn == len(moveList) - 1:
                            print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                            print(game.boardObject)
                            print(game.getCaptureInfo())
                            print(game.currentPlayer.getOpponent() + " player is in check!")
                            print("Available moves:")
                            candidate = getFileDropAvailMoves(game, userInput)
                            for c in candidate:
                                print(c)
                            print(game.currentPlayer.getOpponent() + ">")
                else:
                    if gameTurn == 399:
                        print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                        print(game.boardObject)
                        print(game.getCaptureInfo())
                        game.endGameByStalemate()
                        break
                    elif gameTurn == len(moveList) - 1:
                        print(repr(game.currentPlayer) + " player " + "action: " + " ".join(userInput))
                        print(game.boardObject)
                        print(game.getCaptureInfo())
                        print(game.currentPlayer.getOpponent() + ">")
            gameTurn += 1


def checkInputForMove(userInput):
    """
    :param userInput: user's input
    :return: True if input is valid else False
    """
    if len(userInput) != 3 and len(userInput) != 4:
        return False
    for i in range(1,3):
        if len(userInput[i]) != 2 or userInput[i][0] not in "abcde" or userInput[i][1] not in "12345":
            return False
    if len(userInput) == 4 and userInput[3] != "promote":
        return False
    return True


def checkInputForDrop(userInput):
    """
    :param userInput: user's input
    :return: True if input is valid else False
    """
    if len(userInput) != 3:
        return False
    if len(userInput[2]) != 2 or userInput[2][0] not in "abcde" or userInput[2][1] not in "12345":
        return False
    if userInput[1] not in "gsprn":
        return False
    return True

def handlePromotion(game, userInput):
    """
    Thinking process: A promotion is transferring one to its promoted version.
    It could not happen if piece could not be promoted, or if neither start nor end
    is in promotion zone.
    :param game: the game object
    :param userInput: the user input
    :return: True if an promotion could be made else False.
    """
    starti, startj = game.transForm(userInput[1])
    endi, endj = game.transForm(userInput[2])
    end = game.board[endi][endj]
    targetRow = game.currentPlayer.getPromotionRow()
    if starti != targetRow and endi != targetRow:
        return False
    if not end.getPiece().canPromote:
        return False
    if end.getPiece().ID == id(preview.Preview):
        end.setPiece(promoted_preview.PromotedPreview(end.getPiece().isLower()))
    elif end.getPiece().ID == id(note.Note):
        end.setPiece(promoted_notes.PromotedNotes(end.getPiece().isLower()))
    elif end.getPiece().ID == id(governance.Governance):
        end.setPiece(promoted_governance.PromotedGovernance(end.getPiece().isLower()))
    else:
        end.setPiece(promoted_relay.PromotedRelay(end.getPiece().isLower()))
    return True


def handleDrop(game,userInput):
    """
    Thinking process:
    the piece in capture is already in its unpromoted form and in the right side.
    A piece cannot be dropped if it is not in capture, if the end is occupied by piece.
    or if the piece is preivew and a. it is in promotion zone or 2. it results in immediate checkmate
    3. another preview on the same side is on the same column
    :param game: the game object
    :param userInput: the user input
    :return: True if drop could be made else False
    """
    pieceName = userInput[1]
    piece = game.repr2Piece[pieceName](game.currentPlayer.isLowerSide())
    endi, endj = game.transForm(userInput[2])
    end = game.board[endi][endj]
    if end.getPiece():
        game.endGameByIllegalMove()
        return False
    checkList = [repr(c) for c in game.currentPlayer.captures]
    if " " + pieceName not in checkList:
        game.endGameByIllegalMove()
        return False
    if pieceName == "p":
        if endi == game.currentPlayer.getPromotionRow():
            game.endGameByIllegalMove()
            return False
        tempBoard = copy.deepcopy(game.board)
        tempBoard[endi][endj].setPiece(piece)
        move = Move(game.currentPlayer, game.getOpponent(), game.board, None, end, piece)
        if move.isCheck(tempBoard):
            if move.isCheckMate(tempBoard):
                game.endGameByIllegalMove()
                return False
        if game.currentPlayer == game.upperPlayer:
            target = " P"
        else:
            target = " p"
        for i in range(len(game.board)):
            if game.board[i][endj].getPiece() and repr(game.board[i][endj].getPiece) == target:
                game.endGameByIllegalMove()
                return False
        end.setPiece(piece)
        toRemove = None
        for c in game.currentPlayer.captures:
            if repr(c) == " " + pieceName:
                toRemove = c
                break
        game.currentPlayer.captures.remove(toRemove)
        print(game.boardObject)
        game.getCaptureInfo()
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

def checkFileDropIllegal(game, userInput):
    """
    For file mode, check if a drop is illegal.
    :param game: the game object
    :param userInput: the user input
    :return: True if the drop is illegal else False.
    """
    pieceName = userInput[1]
    if game.currentPlayer == game.upperPlayer:
        rightPieceName = pieceName.upper()
    else:
        rightPieceName = pieceName.lower()
    piece = game.repr2Piece[pieceName](game.currentPlayer.isLowerSide())
    endi, endj = game.transForm(userInput[2])
    end = game.board[endi][endj]
    if end.getPiece():
        return False
    checkList = [repr(c) for c in game.currentPlayer.captures]

    if " " + rightPieceName not in checkList:
        return False
    if pieceName == "p":
        if endi == game.currentPlayer.getPromotionRow():
            return False
        tempBoard = copy.deepcopy(game.board)
        tempBoard[endi][endj].setPiece(piece)
        tempmove = Move(game.currentPlayer, game.getOpponent(), tempBoard, None, end, piece)
        if tempmove.isCheck(tempBoard):
            return False
        if game.currentPlayer == game.upperPlayer:
            target = " P"
        else:
            target = " p"
        for i in range(len(game.board)):
            if game.board[i][endj].getPiece():
                if target == repr(game.board[i][endj].getPiece()):
                    return False
    end.setPiece(piece)
    toRemove = None
    for c in game.currentPlayer.captures:
        if repr(c) == " " + rightPieceName:
            toRemove = c
            break
    game.currentPlayer.captures.remove(toRemove)
    return True


def checkFileDropCheck(game,userInput):
    """
    For file mode, check if a drop results in check.
    :param game: the game object
    :param userInput: the user input
    :return: True if the drop results in check else False.
    """
    pieceName = userInput[1]
    piece = game.repr2Piece[pieceName](game.currentPlayer.isLowerSide())
    endi, endj = game.transForm(userInput[2])
    end = game.board[endi][endj]
    move = Move(game.currentPlayer, game.getOpponent(), game.board, None, end, piece)
    if move.isCheck(game.board):
        return True
    return False

def checkFileDropCheckMate(game, userInput):
    """
    For file mode, check if a drop results in checkmate.
    :param game: the game object
    :param userInput: the user input
    :return: True if the drop results in checkmate else False.
    """
    pieceName = userInput[1]
    piece = game.repr2Piece[pieceName](game.currentPlayer.isLowerSide())
    endi, endj = game.transForm(userInput[2])
    end = game.board[endi][endj]
    move = Move(game.currentPlayer, game.getOpponent(), game.board, None, end, piece)
    if move.isCheckMate(game.board):
        return True
    return False

def getFileDropAvailMoves(game,userInput):
    """
    For file mode, get all the possbile moves for a player to "uncheck".
    :param game: the game object
    :param userInput: the user input
    :return: the list of all possible moves for a player to "uncheck".
    """
    pieceName = userInput[1]
    piece = game.repr2Piece[pieceName](game.currentPlayer.isLowerSide())
    endi, endj = game.transForm(userInput[2])
    end = game.board[endi][endj]
    move = Move(game.currentPlayer, game.getOpponent(), game.board, None, end, piece)
    candidate = move.generateCheckMoves(game.board)
    return candidate


def checkFileMoveIllegal(game, userInput):
    """
    For file mode, check if a move is illegal.
    :param game: the game object
    :param userInput: the user input
    :return: True if the move is illegal else False.
    """
    starti, startj = game.transForm(userInput[1])
    endi, endj = game.transForm(userInput[2])
    start, end = game.board[starti][startj], game.board[endi][endj]
    prev = end.getPiece()
    if prev:
        prevCapture = prev.origin(game.currentPlayer.isLowerSide)
    if game.makeMove(start, end):
        movePreCheck = Move(getOpponent(game), game.getOpponent(), game.board)
        if movePreCheck.isCheck(game.board):
            game.makeMove(end, start)
            return False
        else:
            if len(userInput) == 4:
                if not handlePromotion(game, userInput):
                    game.makeMove(end,start)
                    if prev:
                        end.setPiece(prev)
                        ref = copy.deepcopy(game.currentPlayer.captures)
                        for i in range(len(ref)):
                            if ref[i].ID == prevCapture.ID:
                                game.currentPlayer.captures.pop(i)
                                break
                    return False
            if endi == game.currentPlayer.getPromotionRow() and end.getPiece().ID == id(preview.Preview):
                end.setPiece(promoted_preview.PromotedPreview(end.getPiece().isLower()))
    else:
        return False
    return True

def checkFileMoveCheck(game, userInput):
    """
    For file mode, check if a move results in check.
    :param game: the game object
    :param userInput: the user input
    :return: True if the move results in check else False.
    """
    starti, startj = game.transForm(userInput[1])
    endi, endj = game.transForm(userInput[2])
    start, end = game.board[starti][startj], game.board[endi][endj]
    move = Move(game.currentPlayer, game.getOpponent(), game.board, start, end, None)
    if move.isCheck(game.board):
        return True
    else:
        return False

def checkFileMoveCheckMate(game, userInput):
    """
    For file mode, check if a move results in checkmate.
    :param game: the game object
    :param userInput: the user input
    :return: True if the move results in checkmate else False.
    """
    starti, startj = game.transForm(userInput[1])
    endi, endj = game.transForm(userInput[2])
    start, end = game.board[starti][startj], game.board[endi][endj]
    move = Move(game.currentPlayer, game.getOpponent(), game.board, start, end, None)
    if move.isCheckMate(game.board):
        return True
    else:
        return False

def getFileMoveAvailMoves(game, userInput):
    """
    For file mode, get all the possbile moves for a player to "uncheck".
    :param game: the game object
    :param userInput: the user input
    :return: the list of all possible moves for a player to "uncheck".
    """
    starti, startj = game.transForm(userInput[1])
    endi, endj = game.transForm(userInput[2])
    start, end = game.board[starti][startj], game.board[endi][endj]
    move = Move(game.currentPlayer, game.getOpponent(), game.board, start, end, None)
    candidate = move.generateCheckMoves(game.board)
    return candidate


def handlePlayerMove(game, userInput):
    """
    Given a move the user attempts to make, if the move is valid, make it, and print the according result.
    :param game: the game object
    :param userInput: the user input
    :return: True if the move could be made else False
    """
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
    game.getCaptureInfo()
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
    """
    :param game: the input game object
    :return: the current player in game's opponent
    """
    return game.getOpponent()


if __name__ == main():
    main()













