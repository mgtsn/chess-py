from .piece import *


class King(Piece):
    names = ["K", "k"]

    def moves_from_position(self, board, position):
        moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                new_x_pos = position[0] + x
                new_y_pos = position[1] + y
                if self._valid_target(board, [new_x_pos, new_y_pos]):
                    moves.append([new_x_pos, new_y_pos])
        return moves
