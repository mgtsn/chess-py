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

        target = board[position[0]][position[1] + direction]
        if target == []:
            moves.append([position[0], position[1] + direction])

        for i in [-1, 1]:
            target = board[position[0] + i][position[1] + direction]
            if target != []:
                if target.color != self.color:
                    moves.append([position[0] + i, position[1] + direction])

        return moves
