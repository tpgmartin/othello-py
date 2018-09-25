import math
from string import ascii_lowercase
import sys

from board import Board

class Game():

    def __init__(self):
        self.board = Board()
        self.current_player_turn = "Dark"
        self.player_turn()

    def player_turn(self):
        player_prompt = self.current_player_turn + " player turn ..."
        player_turn = input(player_prompt)

        if not self.check_move_valid(player_turn):
            self.player_turn()

        output = self.current_player_turn + " player chose " + str(player_turn)
        print(output)

    def check_move_valid(self, move):
        return self.__check_move_format(move) and self.__check_move_legal(move)

    # Add additional console messages
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

        neighbouring_opponent_pieces = self.__check_neighbouring_pieces(move)
        return neighbouring_opponent_pieces and self.__check_ending_piece(move, neighbouring_opponent_pieces)

    def __check_neighbouring_pieces(self, move):

        row_index = int(move[0])
        column_index = ascii_lowercase[0:8].index(move[1])
        neighbouring_opponent_pieces = []

        for row in range(row_index-1,row_index+2):
            for column in range(column_index-1,column_index+2):
                opponent_piece_colour = "l" if self.current_player_turn == "Dark" else "d"
                if self.board.positions[row][column] == opponent_piece_colour:
                    opponent_piece = {
                        "column_index": column,
                        "row_index": row
                    }
                    neighbouring_opponent_pieces.append(opponent_piece)

        if len(neighbouring_opponent_pieces) == 0:
            return False

        return neighbouring_opponent_pieces

    def __check_ending_piece(self, move, neighbouring_opponent_pieces):
        new_row_index = int(move[0])
        new_column_index = ascii_lowercase[0:8].index(move[1])

        new_piece_position = 8 * (new_row_index % 8) + new_column_index

        for opponent_piece in neighbouring_opponent_pieces:
            opponent_row_index = opponent_piece["row_index"]
            opponent_column_index = opponent_piece["column_index"]
            opponent_piece_position = 8 * (opponent_row_index % 8) + opponent_column_index

            position_to_check = 2 * opponent_piece_position - new_piece_position
            current_player_piece_colour = self.current_player_turn[0].lower()
            while position_to_check > 0:
                column = position_to_check % 8
                row = math.floor(position_to_check / 8)
                if self.board.positions[row][column] == current_player_piece_colour:
                    return True
                elif self.board.positions[row][column] == None:
                    return False
                position_to_check - relative_position
            
            return False

if __name__ == "__main__":
    Game()