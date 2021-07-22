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

<<<<<<< HEAD
        white_pieces = [
            Rook(0),
            Knight(0),
            Bishop(0),
            King(0),
            Queen(0),
            Bishop(0),
            Knight(0),
            Rook(0)
        ]
        black_pieces = [
            Rook(1),
            Knight(1),
            Bishop(1),
            King(1),
            Queen(1),
            Bishop(1),
            Knight(1),
            Rook(1)
        ]
=======
        piece_order = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
>>>>>>> 19c7bcd748b47b7e4d5cd6087961520bbf67a65c

        for i in range(8):
            board[i][0] = piece_order[i](0, [i, 0])
            board[i][7] = piece_order[i](1, [i, 7])

            board[i][1] = Pawn(0, [i, 1])
            board[i][6] = Pawn(1, [i, 6])
        return board

    def __init__(self):
        self.current_player = 0
        self.board = self.build_board()

    # display the board using the names of pieces, O for empty square
    def print_board(self):
        for j in reversed(range(8)):
            p = f"{j + 1} | "
            for i in range(8):
                try:
                    p += f"{self.board[i][j].name} "
                except:
                    p += "O "
            print(p)
        print("    - - - - - - - - ")
        print("    A B C D E F G H ")

    # returns a list holding all pieces of given color
    def get_pieces(self, player):
        pieces = []
        for i in self.board:
            for j in i:
                if j != []:
                    if j.color == player:
                        pieces.append(j)
        return pieces

    def find_king(self, player):
        for i in range(8):
            for j in range(8):
                p = self.board[i][j]
                if type(p) == King:
                    if p.color == player:
                        return [i, j]
        return 0

    def in_check(self):
        pieces = get_pieces((self.current_player + 1) % 2)
        king_location = self.find_king(self.current_player)
        return True

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
                formatted_move.append([m1, m2])
        else:
            print("Incorrect Format")
        return formatted_move

    # determine if given move is legal in rules of the game
    def legal_move(self, move):
        current = move[0]
        target = move[1]
        moving_piece = self.board[current[0]][current[1]]
        target_piece = self.board[target[0]][target[1]]

<<<<<<< HEAD
        print(
            f"possible moves: {moving_piece.moves_from_position(self.board, current)}"
        )
=======
        moving_piece.legal_moves(self.board)
>>>>>>> 19c7bcd748b47b7e4d5cd6087961520bbf67a65c

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

    # makes the move, updating piece locations
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
            print(f"Player move: {player_move}")
            if self.legal_move(player_move):
                self.make_move(player_move)
                return

    def game_finished(self):
        return False

    # loop through player's turns taking input until game is finished
    def play(self):
        finished = False
        while not finished:
            self.print_board()
            print(f"Player {self.current_player + 1}'s turn")

            self.get_player_move()

            self.switch_player()

            # finished = True

