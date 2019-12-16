import drive
import governance


class PromotedGovernance(governance.Governance, drive.Drive):
    def __init__(self, lowerSide):
        self.promoted = True
        self.origin = governance.Governance
        self.lowerSide = lowerSide

    def __repr__(self):
        if self.lowerSide:
            return "+g"
        else:
            return "+G"

    def generatePossibleMoves(self, board, start):
        g = governance.Governance(self.lowerSide)
        d = drive.Drive(self.lowerSide)
        choice1 = g.generatePossibleMoves(board, start)
        choice2 = d.generatePossibleMoves(board, start)
        return list(set(choice1 + choice2))

    def canMove(self, player, board, start, end, changeCapture = True):
        if not self.checkMoveBasics(start, end):
            return False
        allMoves = self.generatePossibleMoves(board, start)
        if end not in allMoves:
            return False
        if end.getPiece():
            if changeCapture:
                player.setCapture(end.getPiece().origin(player.lowerSide))
        end.setPiece(start.getPiece())
        start.setPiece(None)
        return True


