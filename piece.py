from abc import ABCMeta, abstractmethod


class Piece(object):
    """
    Class that represents a BoxShogi piece
    """
    __metaclass__ = ABCMeta

    def __init__(self, lowerSide):
        self.lowerSide = lowerSide
        self.captured = False
        self.canPromote = False
        self.promoted = False

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def canMove(self, player, board, start, end):
        pass

    @abstractmethod
    def generatePossibleMoves(self, board, start):
        pass

    def checkMoveBasics(self, start, end):
        if not start.getPiece():
            return False
        if end.getPiece() and start.getPiece().isLower() == end.getPiece().isLower():
            return False
        if start.getX() < 0 or start.getX() > 4 or start.getY() < 0 or start.getY() > 4:
            return False
        if end.getX() < 0 or end.getX() > 4 or end.getY() < 0 or start.getY() > 4:
            return False
        return True

    def checkPromote(self):
        return self.canPromote

    def isLower(self):
        return self.lowerSide

    def isCaptured(self):
        return self.captured

    def capture(self):
        self.captured = True







