from .piece import *


class Rook(Piece):
    names = ["R", "r"]

    def can_make_move(self, board, move):
        return(self.vertical_movement(board, move) or self.horizontal_movement(board, move))
