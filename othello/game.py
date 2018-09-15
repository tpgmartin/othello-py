from string import ascii_lowercase
import sys

from board import Board

class Game():

    def __init__(self):
        self.board = Board()
        self.dark_player_turn()

    def dark_player_turn(self):
        dark_player_turn = input("Dark player turn ...")

        if not self.check_move_valid(dark_player_turn):
            print('Invalid move')
            self.dark_player_turn()

        print("Dark player chose", str(dark_player_turn))

    def check_move_valid(self, move):
        return self.__check_move_format(move) and self.__check_move_legal(move)

    def __check_move_format(self, move):
        try:
            number = int(move[0])
        except ValueError:
            return False

        letter = move[1]

        if number not in range(8):
            return False

        if letter not in list(ascii_lowercase[0:8]):
            return False

        return True

    def __check_move_legal(self, move):

        row_index = int(move[0])
        column_index = ascii_lowercase[0:8].index(move[1])

        return self.__check_neighbouring_pieces(move)

    def __check_neighbouring_pieces(self, move):

        neighbouring_pieces = []
        row_index = int(move[0])
        column_index = ascii_lowercase[0:8].index(move[1])

        # Need to handle case where moving to edge of board
        target_rows = self.board.positions[row_index-1:row_index+2]

        for row in target_rows:
            neighbouring_pieces.append(row[column_index-1:column_index+2])

        neighbouring_pieces = [item for sublist in neighbouring_pieces for item in sublist]

        # Only consider dark player turn for time being
        if 'l' not in neighbouring_pieces:
            return False

        return True

    # Valid moves in Othello
    # * Must be next to piece of other colour
    # * Must exist straight line from position of new piece to
    #   another piece of same colour

if __name__ == "__main__":
    Game()