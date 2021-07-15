from pieces import Game

g = Game()
# g.play()

for p in g.get_pieces(1):
    print(p.name)
