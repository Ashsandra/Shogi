from abc import ABC, abstractmethod


class Piece(ABC):
    """
    Class that represents a BoxShogi piece
    """
    def __init__(self, lowerSide):
        self.lowerSize = lowerSide
        self.captured = False
        self.promoted = False

    def isLower(self):
        return self.lowerside

    def isCaptured(self):
        return self.captured

    def capture(self):
        self.captured = True

    @abstractmethod
    def canMove(self, board, start, end):
        pass



