from .piece import *


class Bishop(Piece):
    names = ["B", "b"]

    def moves_from_position(self, board, position):
        return self._diagonal_moves_from_position(board, position)