from string import ascii_lowercase
import sys

from board import Board

class Game():

    def __init__(self):
        self.dark_player_turn()

    def dark_player_turn(self):
        dark_player_turn = input("Dark player turn ...")

        if not self.check_valid_move(dark_player_turn):
            print('Invalid move')
            self.dark_player_turn()

        print("Dark player chose", str(dark_player_turn))

    @staticmethod
    def check_valid_move(turn):

        try:
            number = int(turn[0])
        except ValueError:
            return False

        letter = turn[1]

        if number not in range(8):
            return False

        if letter not in list(ascii_lowercase[0:8]):
            return False

        return True

if __name__ == "__main__":
    Game()