from .piece import *


class King(Piece):
    names = ["K", "k"]

    def can_make_move(self, board, move):
        current = move[0]
        target = move[1]

        diff_x = abs(current[0] - target[0])
        diff_y = abs(current[1] - target[1])

        return(diff_x <= 1 and diff_y <= 1)
