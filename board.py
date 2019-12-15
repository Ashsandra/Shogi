import os
import copy
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

    def __init__(self):
        self._board = self._initEmptyBoard()


    def getBoard(self):
        return self._board

    def _initEmptyBoard(self):
        # TODO: Initalize empty board
        # 0,0 - 0,
        board = [[Square(None,i,j) for j in range(5)] for i in range(5)]
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
        return self._stringifyBoard(self.rotate90Clockwise(copy.deepcopy(self._board)))

    def _stringifyBoard(self, board):
        """
        Utility function for printing the board
        """
        s = ''
        for row in range(len(board) - 1, -1, -1):
            s += '' + str(row + 1) + ' |'
            for col in range(0, len(board[row])):
                s += self._stringifySquare(board[col][row])
            s += os.linesep

        s += '    a  b  c  d  e' + os.linesep
        return s

    def rotate90Clockwise(self,A):

        N = len(A[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[i][j]
                A[i][j] = A[N - 1 - j][i]
                A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
                A[j][N - 1 - i] = temp
        return A

    def _stringifySquare(self, sq):
        """
       	Utility function for stringifying an individual square on the board

        :param sq: Array of strings.
        """
        if sq.getPiece():
            sq = repr(sq.getPiece())
        else:
            sq = "__"
        if type(sq) is not str or len(sq) > 2:
            raise ValueError('Board must be an array of strings like "", "P", or "+P"')
        if len(sq) == 0:
            return '__|'
        if len(sq) == 1:
            return ' ' + sq + '|'
        if len(sq) == 2:
            return sq + '|'
