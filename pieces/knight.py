from .piece import *
import math


class Knight(Piece):
    names = ["N", "n"]

    def can_make_move(self, board, move):
        current = move[0]
        target = move[1]

        diff_x = abs(current[0] - target[0])
        diff_y = abs(current[1] - target[1])

        return (diff_x == 1 and diff_y == 2 or diff_x == 2 and diff_y == 1)

    def moves_from_position(self, board, positon):
        moves = []
        for i in [-1, 1]:
            for j in [-2, 2]:
                new_x_pos = positon[0] + i
                new_y_pos = positon[1] + j
                if self.valid_target(board, [new_x_pos, new_y_pos]):
                    moves.append([new_x_pos, new_y_pos])

                new_x_pos = positon[0] + j
                new_y_pos = positon[1] + i
                if self.valid_target(board, [new_x_pos, new_y_pos]):
                    moves.append([new_x_pos, new_y_pos])
        return moves
