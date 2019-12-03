import os


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

    def _initEmptyBoard(self):
        # TODO: Initalize empty board
        global BOARD_SIZE
        global INIT_POSITIONS
        board = [["__" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        for i, j in INIT_POSITIONS:
            board[i][j] = INIT_POSITIONS[(i,j)]
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
        if type(sq) is not str or len(sq) > 2:
            raise ValueError('Board must be an array of strings like "", "P", or "+P"')
        if len(sq) == 0:
            return '__|'
        if len(sq) == 1:
            return ' ' + sq + '|'
        if len(sq) == 2:
            return sq + '|'
