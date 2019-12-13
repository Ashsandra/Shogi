class Player:
    def __init__(self, lowerSide):
        self.lowerSide = lowerSide
        self.captures = []

    def isLowerSide(self):
        return self.lowerSide

    def getCapture(self):
        return self.captures

    def setCapture(self, piece):
        self.captures.append(piece)








