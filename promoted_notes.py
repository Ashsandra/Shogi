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

    def canMove(self, player, board, start, end):
        return Note.canMove(player, board, start, end) or Drive.canMove(player, board, start, end)