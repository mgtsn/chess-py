import copy


class Piece:

    names = ["X", "x"]

    def __init__(self, color):
        self.color = color
        self.name = self.names[color]

    # true if target space is empty or your opponents piece
    def _valid_target(self, board, position):
        x = position[0]
        y = position[1]
        if range(0, 8).__contains__(x) and range(0, 8).__contains__(y):
            target = board[x][y]
            if target == []:
                return True
            elif target.color != self.color:
                return True

    def _vertical_moves_from_position(self, board, position):
        moves = []
        for i in [-1, 1]:
            y_branch = copy.copy(position)
            searching = True
            while searching:
                y_branch[1] += i
                if y_branch[1] > 7 or y_branch[1] < 0:
                    searching = False
                else:
                    current_square = board[y_branch[0]][y_branch[1]]
                    if current_square == []:
                        moves.append(copy.copy(y_branch))
                    elif current_square.color == self.color:
                        searching = False
                    else:
                        moves.append(y_branch)
                        searching = False
        return moves

    def _horizontal_moves_from_position(self, board, position):
        moves = []
        for i in [-1, 1]:
            x_branch = copy.copy(position)
            searching = True
            while searching:
                x_branch[0] += i
                if x_branch[0] > 7 or x_branch[0] < 0:
                    searching = False
                else:
                    current_square = board[x_branch[0]][x_branch[1]]
                    if current_square == []:
                        moves.append(copy.copy(x_branch))
                    elif current_square.color == self.color:
                        searching = False
                    else:
                        moves.append(x_branch)
                        searching = False
        return moves

    #return all straight moves piece can make: used for queen and rook
    def _straight_moves_from_position(self, board, position):
        return self._vertical_moves_from_position(
            board, position) + self._horizontal_moves_from_position(
                board, position)

    #return all diagonal moves piece can make: used for queen and bishop
    def _diagonal_moves_from_position(self, board, position):
        moves = []
        for x in [-1, 1]:
            for y in [-1, 1]:
                searching_branch = True
                new_x_pos = position[0] + x
                new_y_pos = position[1] + y
                while searching_branch:
                    if self._valid_target(board, [new_x_pos, new_y_pos]):
                        moves.append([new_x_pos, new_y_pos])
                        if board[new_x_pos][new_y_pos] != []:
                            searching_branch = False
                        new_x_pos += x
                        new_y_pos += y

                    else:
                        searching_branch = False

        return moves

    #return a list of all positions this piece could move to from the given position
    def moves_from_position(self, board, position):
        return []