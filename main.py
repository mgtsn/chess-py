from pieces import Game


def main():
    game = Game()
    while not game.finished:
        game.print_board(game.board)
        print(f"\nPlayer {game.current_player + 1}'s turn")
        game.take_turn()


if __name__ == "__main__":
    main()