class Piece:

    names = ["X", "x"]

    def __init__(self, color):
        self.color = color
        self.name = self.names[color]

    def straight_movement(self, board, move):
        possible_moves = []
        current = move[0]
        target = move[1]

    def vertical_movement(self, board, move):
        current = move[0]
        target = move[1]

        if current[1] != target[1]:
            return False

        for i in range(min(current[0], target[0]) + 1, max(current[0], target[0])):
            n = board[i][current[1]]
            if n != []:
                return False
        return True

    def horizontal_movement(self, board, move):
        current = move[0]
        target = move[1]

        if current[0] != target[0]:
            return False

        for i in range(min(current[1], target[1]) + 1, max(current[1], target[1])):
            n = board[current[0]][i]
            if n != []:
                return False
        return True

    def diagonal_movement(self, board, move):
        current = move[0]
        target = move[1]

        diff_x = abs(current[0] - target[0])
        diff_y = abs(current[1] - target[1])

        if diff_x != diff_y:
            return False

        return True

    def can_make_move(self, board, move):
        print("Can make move?")
        return True
