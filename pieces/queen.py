from .piece import *


class Queen(Piece):
    names = ["Q", "q"]

    def moves_from_position(self, board, position):
        return self._diagonal_moves_from_position(
            board, position) + self._straight_moves_from_position(
                board, position)
