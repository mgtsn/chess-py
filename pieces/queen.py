from .piece import *


class Queen(Piece):
    names = ["Q", "q"]

    def can_make_move(self, board, move):
        return(self.horizontal_movement(board, move) or self.vertical_movement(board, move)
               or self.diagonal_movement(board, move))
