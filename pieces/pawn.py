from .piece import *


class Pawn(Piece):
    names = ["P", "p"]

    def can_make_move(self, board, move):
        current = move[0]
        target = move[1]

        if self.color == 0:
            direction = 1
        else:
            direction = -1

        if target[1] == current[1] + direction:
            if target[0] == current[0] and board[target[0]][target[1]] == []:
                return True
            if target[0] == current[0] + 1 or target[1] == current[1] - 1:
                if board[target[0]][target[1]] != []:
                    return True
        return False

    def moves_from_position(self, board, position):
        moves = []

        if self.color == 0:
            direction = 1
        else:
            direction = -1

        new_x_pos = position[0]
        new_y_pos = position[1] + direction
        if not range(0, 8).__contains__(new_y_pos):
            return moves

        target = board[new_x_pos][new_y_pos]
        if target == []:
            moves.append([new_x_pos, new_y_pos])

        for i in [-1, 1]:
            new_x_pos = position[0] + i
            if range(0, 8).__contains__(new_x_pos):
                target = board[new_x_pos][new_y_pos]
                if target != []:
                    if target.color != self.color:
                        moves.append([new_x_pos, new_y_pos])

        return moves
