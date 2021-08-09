from .piece import *


class Rook(Piece):
    names = ["R", "r"]

    def moves_from_position(self, board, position):
        return (self._straight_moves_from_position(board, position))
