class Piece:

    names = ["X", "x"]

    def __init__(self, color):
        print()
        self.color = color
        self.name = self.names[color]
