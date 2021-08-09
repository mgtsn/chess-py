from .piece import *


class Pawn(Piece):
    names = ["P", "p"]

    def __init__(self, color):
        super().__init__(color)
        self.can_move_double = True

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

        #looks two spaces ahead if has not moved yet
        if self.can_move_double:
            target = board[new_x_pos][new_y_pos + direction]
            if target == []:
                moves.append([new_x_pos, new_y_pos + direction])

        #can move one space ahead if is empty
        target = board[new_x_pos][new_y_pos]

        if target == []:
            moves.append([new_x_pos, new_y_pos])

        #can move diagonally forward if taking a piece
        for i in [-1, 1]:
            new_x_pos = position[0] + i
            if range(0, 8).__contains__(new_x_pos):
                target = board[new_x_pos][new_y_pos]
                if target != []:
                    if target.color != self.color:
                        moves.append([new_x_pos, new_y_pos])

        return moves
