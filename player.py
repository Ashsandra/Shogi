class Player:
    """
    Class that represents a player in the game.
    """
    def __init__(self, lowerSide):
        self.lowerSide = lowerSide
        self.captures = []

    def __repr__(self):
        if self.lowerSide:
            return "lower"
        else:
            return "UPPER"

    def isLowerSide(self):
        """
        :return: the side of the player (upper or lower).
        """
        return self.lowerSide

    def getPromotionRow(self):
        """
        :return: get the promotion row number for upper player/lower player.
        """
        if self.isLowerSide():
            return 0
        else:
            return 4

    def getOpponent(self):
        """
        :return: The name of the player's opponent.
        """
        return "UPPER" if self.lowerSide else "lower"

    def getCapture(self):
        """
        :return: pieces captured by the player.
        """
        return self.captures

    def setCapture(self, piece):
        """
        :param piece: piece to be appended to the capture list
        :return: None
        """
        self.captures.append(piece)








