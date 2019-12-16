import drive
import note


class PromotedNotes(note.Note, drive.Drive):
    def __init__(self, lowerSide):
        self.canPromote = False
        self.origin = note.Note
        self.lowerSide = lowerSide
        self.ID = id(PromotedNotes)

    def __repr__(self):
        if self.lowerSide:
            return "+n"
        else:
            return "+N"

    def generatePossibleMoves(self, board, start):
        d = drive.Drive(self.lowerSide)
        n = note.Note(self.lowerSide)
        choice1 = n.generatePossibleMoves(board, start)
        choice2 = d.generatePossibleMoves(board, start)
        return list(set(choice1 + choice2))

    def canMove(self, player, board, start, end, changeCapture = True):
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