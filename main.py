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

        board[0] = []
        board[7] = []

        for i in range(8):
            board[1][i] = Pawn(0)
            board[6][i] = Pawn(1)
        return board

    def __init__(self):
        self.name = "board"
        self.board = self.build_board()


# c = Game()
# print(c.name)
# print(c.board)

x = Piece(0)
print(x.name)

p = Pawn(0)
print(p.name)
print(p.color)
