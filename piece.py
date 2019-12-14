from abc import ABC, abstractmethod


class Piece(ABC):
    """
    Class that represents a BoxShogi piece
    """
    def __init__(self, lowerSide):
        self.lowerSize = lowerSide
        self.captured = False
        self.canPromote = False
        self.promoted = False

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def canMove(self, player, board, start, end):
        pass

    def checkMoveBasics(self, start, end):
        if start == end:
            return False
        if start.getPiece().isLower == end.getPiece().isLower:
            return False
        if start.getX() < 0 or start.getX() > 4 or start.getY() < 0 or start.getY() < 4:
            return False
        if end.getX() < 0 or end.getX() > 4 or end.getY() < 0 or start.getY() < 4:
            return False
        return True

    def checkPromote(self):
        return self.canPromote

    def isLower(self):
        return self.lowerside

    def isCaptured(self):
        return self.captured

    def capture(self):
        self.captured = True







