from drive import Drive
from note import Note


class PromotedNotes(Note, Drive):
    def __init__(self):
        self.self.promoted = True
        self.origin = Note

    def __repr__(self):
        if self.lowerSide:
            return "+n"
        else:
            return "+N"

    def generatePossibleMoves(self, board, start):
        choice1 = Note.generatePossibleMoves(board, start)
        choice2 = Drive.generatePossibleMoves(board, start)
        return list(set(choice1 + choice2))

    def canMove(self, player, board, start, end):
        return Note.canMove(player, board, start, end) or Drive.canMove(player, board, start, end)