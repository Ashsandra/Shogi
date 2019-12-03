class Piece:
    """
    Class that represents a BoxShogi piece
    """

    INIT_PIECES = ["D", "R", "G", "S", "N", "P", "d", "r", "g", "s", "n", "p"]
    PROMOTED_PIECES = ["+r", "+g", "+n", "+p","+R", "+G", "+N", "+P"]


    def __init__(self, piece_type):
        self.piece_type = piece_type

    def __repr__(self):
        global PROMOTED_PIECES
        return self.piece_type if self.piece_type in PROMOTED_PIECES else "_" + self.piece_type

    def possible_next_positions(self):
        type = self.piece_type
        pass

    def possible_next_positions_drive(self):
        pass

    def possible_next_positions_governance(self):
        pass

    def possible_next_positions_shield(self):
        pass

    def possible_next_positions_relay(self):
        pass

    def possible_next_positions_preview(self):
        pass

    def possible_next_positions_notes(self):
        pass

