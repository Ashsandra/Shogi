import sys
import board


class Game:

    def __init__(self, mode, filename):
        self.mode = mode

        if mode == "-i":
            self._board = board.Board()

        elif mode == "-f":
            if not filename:
                sys.exit()
            else:
                pass
        else:
            sys.exit()


