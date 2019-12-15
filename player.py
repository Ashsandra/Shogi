class Player:
    def __init__(self, lowerSide):
        self.lowerSide = lowerSide
        self.captures = []

    def __repr__(self):
        if self.lowerSide:
            return "lower"
        else:
            return "UPPER"

    def isLowerSide(self):
        return self.lowerSide

    def getPromotionRow(self):
        if self.isLowerSide():
            return 0
        else:
            return 4

    def getOpponent(self):
        return "UPPER" if self.lowerSide else "lower"

    def getCapture(self):
        return self.captures

    def setCapture(self, piece):
        self.captures.append(piece)








