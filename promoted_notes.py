import drive
import note


class PromotedNotes(note.Note, drive.Drive):
    def __init__(self, lowerSide):
        self.promoted = True
        self.origin = note.Note
        self.lowerSide = lowerSide

    def __repr__(self):
        if self.lowerSide:
            return "+n"
        else:
            return "+N"

    def generatePossibleMoves(self, board, start):
        choice1 = note.Note.generatePossibleMoves(board, start)
        choice2 = drive.Drive.generatePossibleMoves(board, start)
        return list(set(choice1 + choice2))

    def canMove(self, player, board, start, end, changeCapture = True):
        return note.Note.canMove(player, board, start, end, changeCapture) or drive.Drive.canMove(player, board, start, end, changeCapture)