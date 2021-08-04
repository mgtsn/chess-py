from . import *
import re
import copy


class Game:

    # create the chess board and populate with starting layout
    def build_board(self):
        board = []
        # makes empty board
        for i in range(8):
            column = []
            for j in range(8):
                column.append([])
            board.append(column)

        piece_order = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]

        for i in range(8):
            board[i][0] = piece_order[i](0)
            board[i][7] = piece_order[i](1)

            board[i][1] = Pawn(0)
            board[i][6] = Pawn(1)
        return board

    def __init__(self):
        self.current_player = 0
        self.board = self.build_board()

    # display the board using the names of pieces, O for empty square
    def print_board(self):
        squares = ["□", "■"]
        for j in reversed(range(8)):
            p = f"{j + 1} | "
            for i in range(8):
                try:
                    p += f"{self.board[i][j].name} | "
                except:
                    # p += f"{squares[(i + j)%2]} | "
                    p += "  | "
            print(p)
            print(f"   {'----' * 8}")
        print("    A   B   C   D   E   F   G   H   ")

    # returns a list holding all pieces of given color
    def get_pieces(self, player):
        pieces = []
        for i in self.board:
            for j in i:
                if j != []:
                    if j.color == player:
                        pieces.append(j)
        return pieces

    # returns a copy of the board with given move made
    def make_move(self, move):
        new_board = copy.deepcopy(self.board)
        current = move[0]
        target = move[1]
        new_board[target[0]][target[1]] = new_board[current[0]][current[1]]
        new_board[current[0]][current[1]] = []
        return new_board

    #return location of given player's king
    def find_king(self, player, board):
        for i in range(8):
            for j in range(8):
                p = board[i][j]
                if type(p) == King:
                    if p.color == player:
                        return [i, j]
        return 0

    #Check if any of opponent's pieces can move to current player's king
    def in_check(self, board, player):
        king_location = self.find_king(player, board)
        for i in range(8):
            for j in range(8):
                current_piece = board[i][j]
                if current_piece != []:
                    if current_piece.color != player:
                        if current_piece.moves_from_position(
                                board, [i, j]).__contains__(king_location):
                            return True
        return False

    #look at each move each of player's pieces can make. If one moves out of check, then player is not in checkmate
    def in_checkmate(self, board, player):
        for i in range(8):
            for j in range(8):
                current_piece = board[i][j]
                if current_piece != []:
                    if current_piece.color == player:
                        possible_moves = current_piece.moves_from_position(
                            board, [i, j])
                        for move in possible_moves:
                            new_board = self.make_move([[i, j], move])
                            if not self.in_check(new_board, player):
                                return False
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

    def puts_self_in_check(self, move, player):
        new_board = self.make_move(move)
        return self.in_check(new_board, player)

    # determine if given move is legal in rules of the game
    def legal_move(self, move):
        current = move[0]
        target = move[1]
        moving_piece = self.board[current[0]][current[1]]
        target_piece = self.board[target[0]][target[1]]

        if not moving_piece:
            print("No piece at that location")
            return False

        if moving_piece.color != self.current_player:
            print("Not your piece")
            return False

        if not moving_piece.moves_from_position(self.board,
                                                current).__contains__(target):
            print("Illegal Move")
            return False

        if self.puts_self_in_check(move, self.current_player):
            print("Puts you in check")
            return False

        return True

    def get_player_move(self):
        while True:
            player_move = []
            while not player_move:
                player_move = self.format_move(input("Enter your move: "))
            if self.legal_move(player_move):
                self.board = self.make_move(player_move)
                return

    def game_finished(self):
        return False

    # loop through player's turns taking input until game is finished
    def play(self):
        finished = False
        while not finished:
            self.print_board()
            print(f"\nPlayer {self.current_player + 1}'s turn")

            self.get_player_move()

            self.switch_player()

            if self.in_check(self.board, self.current_player):
                if self.in_checkmate(self.board, self.current_player):
                    print(f"Player {self.current_player + 1} in checkmate!")
                    finished = True
                else:
                    print(f"Player {self.current_player} in check!")