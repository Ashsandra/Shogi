from governance import Governance
from drive import Drive


class PromotedGovernance(Governance, Drive):
    def __init__(self):
        self.self.promoted = True
        self.origin = Governance

    def __repr__(self):
        if self.lowerSide:
            return "+g"
        else:
            return "+G"

    def canMove(self, player, board, start, end):
        return Governance.canMove(player, board, start, end) or Drive.canMove(player, board, start, end)


