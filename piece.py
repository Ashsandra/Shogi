class Piece:
    """
    Class that represents a BoxShogi piece
    """

    INIT_PIECES = ["D", "R", "G", "S", "N", "P", "d", "r", "g", "s", "n", "p"]
    PROMOTED_PIECES = ["+r", "+g", "+n", "+p", "+R", "+G", "+N", "+P"]

    def __init__(self, piece_type):
        self.piece_type = piece_type

    def __repr__(self):
        return self.piece_type

    def possibleNextPositions(self):
        type = self.piece_type
        pass

    def possibleNextPositionsDrive(self):
        pass

    def possibleNextPositionsShield(self):
        pass

    def possibleNextPositionsGovernance(self):
        pass

    def possibleNextPositionsPreview(self):
        pass

    def possibleNextPositionsRelay(self):
        pass

    def possibleNextPositionsNote(self):
        pass

