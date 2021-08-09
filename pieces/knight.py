from .piece import *
import math


class Knight(Piece):
    names = ["N", "n"]

    def moves_from_position(self, board, positon):
        moves = []
        for i in [-1, 1]:
            for j in [-2, 2]:
                new_x_pos = positon[0] + i
                new_y_pos = positon[1] + j
                if self._valid_target(board, [new_x_pos, new_y_pos]):
                    moves.append([new_x_pos, new_y_pos])

                new_x_pos = positon[0] + j
                new_y_pos = positon[1] + i
                if self._valid_target(board, [new_x_pos, new_y_pos]):
                    moves.append([new_x_pos, new_y_pos])
        return moves
