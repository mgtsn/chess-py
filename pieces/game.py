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

    # check player input is in correct format, then comvert to a pair of tuples of ints
    def format_move(self, m):
        formatted_move = []
        if re.fullmatch("\w\d\s\w\d", m):
            m = m.split()
            for i in m:
                m1 = ord(i[0].lower()) - 97
                m2 = int(i[1]) - 1
                if m1 < 0 or m1 > 7 or m2 < 0 or m2 > 7:
                    return
                formatted_move.append([m1, m2])
        return formatted_move

    # determine if given move is legal in rules of the game
    def legal_move(self, move):
        return True

    # loop through player's turns taking input until game is finished
    def play(self):
        playing = True
        while playing:
            self.print_board()
            print(f"Player {self.current_player + 1}'s turn")

            player_move = []
            while not player_move:
                player_move = self.format_move(input("Enter your move: "))
                if not self.legal_move(player_move):
                    player_move = []

            print(player_move)
            self.switch_player()
