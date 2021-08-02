from .piece import *


class King(Piece):
    names = ["K", "k"]

    def can_make_move(self, board, move):
        current = move[0]
        target = move[1]

        diff_x = abs(current[0] - target[0])
        diff_y = abs(current[1] - target[1])

        return (diff_x <= 1 and diff_y <= 1)

    def moves_from_position(self, board, position):
        moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                new_x_pos = position[0] + x
                new_y_pos = position[1] + y
                if range(0, 8).__contains__(new_x_pos) and range(
                        0, 8).__contains__(new_y_pos):
                    target = board[new_x_pos][new_y_pos]
                    if target == []:
                        moves.append([new_x_pos, new_y_pos])
                    elif target.color != self.color:
                        moves.append([new_x_pos, new_y_pos])
        return moves
