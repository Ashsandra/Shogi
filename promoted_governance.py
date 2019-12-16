import drive
import governance


class PromotedGovernance(governance.Governance, drive.Drive):
    """
    Class that represents a promoted governance piece.
    """
    def __init__(self, lowerSide):
        self.canPromote = False
        self.origin = governance.Governance
        self.lowerSide = lowerSide
        self.ID = id(PromotedGovernance)

    def __repr__(self):
        if self.lowerSide:
            return "+g"
        else:
            return "+G"

    def generatePossibleMoves(self, board, start):
        """
        :param board: the chess board
        :param start: the starting position
        :return: all valid moves of drive starting from index position.
        """
        g = governance.Governance(self.lowerSide)
        d = drive.Drive(self.lowerSide)
        choice1 = g.generatePossibleMoves(board, start)
        choice2 = d.generatePossibleMoves(board, start)
        return list(set(choice1 + choice2))

    def canMove(self, player, board, start, end, changeCapture = True):
        """
        :param player: the current player
        :param board: the chess board
        :param start: the starting position
        :param end: the ending position
        :param changeCapture: boolean indicating whether the captureList needs to be changed
         :return: whether the player could move from start to end in the given board
        """
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


