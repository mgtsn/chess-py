from piece import *
from pawn import *


class Game:

    # create the chess board and populate with starting layout
    def build_board(self):
        board = []
        # makes empty board
        for i in range(8):
            row = []
            for j in range(8):
                row.append([])
            board.append(row)

        for i in range(8):
            board[1][i] = Pawn()
            board[6][i] = Pawn()
        return board

    def __init__(self):
        self.name = "board"
        self.board = self.build_board()


c = Game()
print(c.name)
# print(c.board)

p = Pawn()
print(p.name)
