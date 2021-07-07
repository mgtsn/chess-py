from pieces import Piece, Pawn, King, Queen, Rook, Knight, Bishop


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
            board[1][i] = Pawn(0)
            board[6][i] = Pawn(1)
        return board

    def __init__(self):
        self.current_player = 0
        self.board = self.build_board()

    def turn(self):
        print(f"current player: {self.current_player}")
        self.current_player = (self.current_player + 1) % 2


g = Game()
for _ in range(5):
    g.turn()
