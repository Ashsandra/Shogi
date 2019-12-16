class Square:
    """
    Class that represents a square in the board.
    """
    def __init__(self,piece,x,y):
        self.piece = piece
        self.x = x
        self.y = y

    def __repr__(self):
        """
        :return: conversion form (x,y) coordinate to form like (a5)
        """
        return chr(self.y + 97) + str(5 - self.x)

    def getPiece(self):
        """
        :return: the piece in the square
        """
        return self.piece

    def setPiece(self, newP):
        """
        :param newP: newPiece to be set
        :return: None
        """
        self.piece = newP

    def getX(self):
        """
        :return: x coordinate
        """
        return self.x

    def getY(self):
        """
        :return: y coordinate
        """
        return self.y

    def setX(self, newX):
        """
        :param newX: new x coordiante to be set
        :return: None
        """
        self.x = newX

    def setY(self,newY):
        """
        :param newY: new y coordiante to be set
        :return: None
        """
        self.y = newY
