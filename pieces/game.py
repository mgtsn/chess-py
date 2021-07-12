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

        board[0] = [Rook(0), Knight(0), Bishop(0), King(
            0), Queen(0), Bishop(0), Knight(0), Rook(0)]
        board[7] = [Rook(1), Knight(1), Bishop(1), King(
            1), Queen(1), Bishop(1), Knight(1), Rook(1)]

        for i in range(8):
            board[1][i] = Pawn(0)
            board[6][i] = Pawn(1)
        return board

    def __init__(self):
        self.current_player = 0
        self.board = self.build_board()

    # display the board using the names of pieces, O for empty square
    def print_board(self):
        for row in reversed(self.board):
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
                    print("Out of Range")
                    return
                formatted_move.append([m2, m1])
        else:
            print("Incorrect Format")
        return formatted_move

    # determine if given move is legal in rules of the game
    def legal_move(self, move):
        current = move[0]
        target = move[1]
        moving_piece = self.board[current[0]][current[1]]
        target_piece = self.board[target[0]][target[1]]

        if not moving_piece:
            print("No piece at that location")
            return False

        if not moving_piece.color == self.current_player:
            print("Not your piece")
            return False

        if not moving_piece.can_make_move(self.board, move):
            print("Illegal Move")
            return False

        if target_piece != []:
            if target_piece.color == self.current_player:
                print("Illegal Move")
                return False
        return True

    def make_move(self, move):
        current = move[0]
        target = move[1]
        self.board[target[0]][target[1]] = self.board[current[0]][current[1]]
        self.board[current[0]][current[1]] = []

    def get_player_move(self):
        while True:
            player_move = []
            while not player_move:
                player_move = self.format_move(input("Enter your move: "))
            if self.legal_move(player_move):
                return player_move

    # loop through player's turns taking input until game is finished
    def play(self):
        playing = True
        while playing:
            self.print_board()
            print(f"Player {self.current_player + 1}'s turn")

            player_move = self.get_player_move()
            self.make_move(player_move)

            self.switch_player()
