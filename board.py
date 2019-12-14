import os
from note import Note
from governance import Governance
from drive import Drive
from preview import Preview
from relay import Relay
from shield import Shield
from square import Square


class Board:
    """
    Class that represents the BoxShogi board
    """

    # The BoxShogi board is 5x5
    BOARD_SIZE = 5
    INIT_POSITIONS = {(0, 0): "N",
                      (0, 1): "G",
                      (0, 2): "R",
                      (0, 3): "S",
                      (0, 4): "D",
                      (1, 4): "P",
                      (3, 0): "p",
                      (4, 0): "d",
                      (4, 1): "s",
                      (4, 2): "r",
                      (4, 3): "g",
                      (4, 4): "n"}

    def __init__(self):
        self._board = self._initEmptyBoard()

    def resetBoard(self):
        return self._board

    def _initEmptyBoard(self):
        # TODO: Initalize empty board
        global BOARD_SIZE
        board = [[Square(None,i,j) for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
        board[0][0] = Square(Note(False), 0, 0)
        board[0][1] = Square(Governance(False), 0, 1)
        board[0][2] = Square(Relay(False), 0, 2)
        board[0][3] = Square(Shield(False), 0, 3)
        board[0][4] = Square(Drive(False), 0, 4)
        board[1][4] = Square(Preview(False), 1, 4)
        board[3][0] = Square(Preview(True), 3, 0)
        board[4][0] = Square(Drive(True), 4, 0)
        board[4][1] = Square(Shield(True), 4, 1)
        board[4][2] = Square(Relay(True), 4, 2)
        board[4][3] = Square(Governance(True), 4, 3)
        board[4][4] = Square(Note(True), 4, 4)
        return board

    def __repr__(self):
        return self._stringifyBoard()

    def _stringifyBoard(self):
        """
        Utility function for printing the board
        """
        s = ''
        for row in range(len(self._board) - 1, -1, -1):
            s += '' + str(row + 1) + ' |'
            for col in range(0, len(self._board[row])):
                s += self._stringifySquare(self._board[col][row])

            s += os.linesep

        s += '    a  b  c  d  e' + os.linesep
        return s

    def _stringifySquare(self, sq):
        """
       	Utility function for stringifying an individual square on the board

        :param sq: Array of strings.
        """
        sq = repr(sq.getPiece())
        if type(sq) is not str or len(sq) > 2:
            raise ValueError('Board must be an array of strings like "", "P", or "+P"')
        if len(sq) == 0:
            return '__|'
        if len(sq) == 1:
            return ' ' + sq + '|'
        if len(sq) == 2:
            return sq + '|'
