from . import *
import re


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

        board[7] = [Rook(0), Knight(0), Bishop(0), King(
            0), Queen(0), Bishop(0), Knight(0), Rook(0)]
        board[0] = [Rook(1), Knight(1), Bishop(1), King(
            1), Queen(1), Bishop(1), Knight(1), Rook(1)]

        for i in range(8):
            board[6][i] = Pawn(0)
            board[1][i] = Pawn(1)
        return board

    def __init__(self):
        self.current_player = 0
        self.board = self.build_board()

    # display the board using the names of pieces, O for empty square
    def print_board(self):
        for row in self.board:
            p = ""
            for i in row:
                try:
                    p += f"{i.name} "
                except:
                    p += "O "
            print(p)

    # change which player is currently active
    def switch_player(self):
        self.current_player = (self.current_player + 1) % 2

    def format_move(self, m):
        formatted_move = []
        if re.fullmatch("\w\d\s\w\d", m):
            # m = m.split()
            for i in m:
                print(f"I: {i}")
        print(m)
        return(formatted_move)

    def play(self):
        print(f"Player {self.current_player + 1}'s turn")
        player_move = []
        while not player_move:
            player_move = self.format_move(input("Enter your move: "))
        self.switch_player()
