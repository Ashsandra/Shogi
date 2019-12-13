class Square:
    def __init__(self,piece,x,y):
        self.piece = piece
        self.x = x
        self.y = y

    def getPiece(self):
        return self.piece

    def setPiece(self, newP):
        self.piece = newP

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, newX):
        self.x = newX

    def setY(self,newY):
        self.y = newY
