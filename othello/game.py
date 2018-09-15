import sys

from board import Board

class Game():

    def __init__(self):
        self.dark_player_turn()

    def dark_player_turn(self):
        dark_player_turn = input("Dark player turn ...")
        check_valid_move(dark_player_turn)
        print("Dark player chose", str(dark_player_turn))

    @staticmethod
    def check_valid_move(turn):
        # Valid move must be of form <number><letter>
        # Where number is between 1-8
        # Where letter is between a-h
        pass

if __name__ == "__main__":
    Game()