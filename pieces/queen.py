from .piece import *


class Queen(Piece):
    names = ["Q", "q"]

    def can_make_move(self, board, move):
        return (self.horizontal_movement(board, move)
                or self.vertical_movement(board, move)
                or self.diagonal_movement(board, move))

    def moves_from_position(self, board, position):
        return self.diagonal_moves_from_position(
            board, position) + self.straight_moves_from_position(
                board, position)
