from . import *
import re
import copy


class Game:

    # create the chess board and populate with starting layout
    def _build_board(self):
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
        self.board = self._build_board()

    # display the board using the names of pieces
    def print_board(self, board):
        print("    A   B   C   D   E   F   G   H   ")
        print(f"   {'----' * 8}")
        for j in reversed(range(8)):
            p = f"{j + 1} | "
            for i in range(8):
                try:
                    p += f"{board[i][j].name} | "
                except:
                    p += "  | "
            p += f"{j + 1}"
            print(p)
            print(f"   {'----' * 8}")
        print("    A   B   C   D   E   F   G   H   ")

    # returns a copy of the board with given move made
    def _make_move(self, move):
        new_board = copy.deepcopy(self.board)
        current = move[0]
        target = move[1]
        new_board[target[0]][target[1]] = new_board[current[0]][current[1]]
        new_board[current[0]][current[1]] = []
        return new_board

    # return location of given player's king
    def _find_king(self, player, board):
        for i in range(8):
            for j in range(8):
                p = board[i][j]
                if type(p) == King:
                    if p.color == player:
                        return [i, j]
        return 0

    # Check if any of opponent's pieces can move to current player's king
    def _in_check(self, board, player):
        king_location = self._find_king(player, board)
        for i in range(8):
            for j in range(8):
                current_piece = board[i][j]
                if current_piece != []:
                    if current_piece.color != player:
                        if current_piece.moves_from_position(
                                board, [i, j]).__contains__(king_location):
                            current_piece.moves_from_position(
                                board, [i, j]).__contains__(king_location)
                            return True
        return False

    # look at each move each of player's pieces can make. If one moves out of check, then player is not in checkmate
    def _in_checkmate(self, board, player):
        for i in range(8):
            for j in range(8):
                current_piece = board[i][j]
                if current_piece != []:
                    if current_piece.color == player:
                        possible_moves = current_piece.moves_from_position(
                            board, [i, j])
                        for move in possible_moves:
                            new_board = self._make_move([[i, j], move])
                            if not self._in_check(new_board, player):
                                return False
        return True

    # change which player is currently active
    def _switch_player(self):
        self.current_player = (self.current_player + 1) % 2

    # check player input is in correct format, then comvert to a pair of tuples of ints
    def _format_move(self, m):
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

    # see if a given move will put you in check
    def _puts_self_in_check(self, move, player):
        new_board = self._make_move(move)
        return self._in_check(new_board, player)

    # determine if given move is legal in rules of the game
    def _legal_move(self, move):
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

        if self._puts_self_in_check(move, self.current_player):
            print("Puts you in check")
            return False

        if type(moving_piece) == Pawn:
            moving_piece.can_move_double = False
        return True

    #read and validate user input
    def get_player_move(self):
        while True:
            player_move = []
            while not player_move:
                player_move = self._format_move(input("Enter your move: "))
            if self._legal_move(player_move):
                self.board = self._make_move(player_move)
                self._switch_player()
                return

    # check if current player is in checkmate, game ends if player is
    def game_finished(self):
        if self._in_check(self.board, self.current_player):
            if self._in_checkmate(self.board, self.current_player):
                print(f"Player {self.current_player + 1} in checkmate!")
                return True
            else:
                print(f"Player {self.current_player + 1} in check!")
                return False