class Piece:

    names = ["X", "x"]

    def __init__(self, color):
        self.color = color
        self.name = self.names[color]

    def horizontal_movement(self, board, move):
        current = move[0]
        target = move[1]

        if current[1] != target[1]:
            return False

        for i in range(min(current[0], target[0]) + 1, max(current[0], target[0])):
            n = board[i][current[1]]
            if n != []:
                return False
        return True

    def vertical_movement(self, board, move):
        current = move[0]
        target = move[1]

        if current[0] != target[0]:
            return False

        for i in range(min(current[1], target[1]) + 1, max(current[1], target[1])):
            n = board[current[0]][i]
            if n != []:
                return False
        return True

    def straight_movement(self, board, move):
        return self.vertical_movement(board, move) and self.horizontal_movement(board, move)

    def diagonal_movement(self, board, move):
        current = move[0]
        target = move[1]

        diff_x = abs(current[0] - target[0])
        diff_y = abs(current[1] - target[1])

        if diff_x == 0 or diff_y == 0:
            return False

        if diff_x != diff_y:
            return False

        dir_x = int((target[0] - current[0]) / diff_x)
        dir_y = int((target[1] - current[1]) / diff_y)

        space = [current[0], current[1]]
        space[0] += dir_x
        space[1] += dir_y

        while space != target:
            if board[space[0]][space[1]] != []:
                return False
            space[0] += dir_x
            current[1] += dir_y
        return True

    def can_make_move(self, board, move):
        return True
