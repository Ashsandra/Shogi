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
        choice1 = governance.Governance.generatePossibleMoves(board, start)
        choice2 = drive.Drive.generatePossibleMoves(board, start)
        return list(set(choice1 + choice2))

    def canMove(self, player, board, start, end, changeCapture = True):
        return governance.Governance.canMove(player, board, start, end,changeCapture)\
               or drive.Drive.canMove(player, board, start, end, changeCapture)


