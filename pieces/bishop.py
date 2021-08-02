from .piece import *


class Bishop(Piece):
    names = ["B", "b"]

    def can_make_move(self, board, move):
        return self.diagonal_movement(board, move)

    def moves_from_position(self, board, position):
        return self.diagonal_moves_from_position(board, position)