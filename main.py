from pieces import Game
import copy


def main():
    game = Game()
    finished = False
    while not finished:
        game.print_board(game.board)
        print(f"\nPlayer {game.current_player + 1}'s turn")

        game.get_player_move()

        game.switch_player()


if __name__ == "__main__":
    main()