from pieces import Game
import copy

g = Game()
# g.play()

print(g.board[0][1].moves_from_position(g.board, [0, 1]))

a = [[0, 1], [1, 2]]
print(a.__contains__([0, 1]))