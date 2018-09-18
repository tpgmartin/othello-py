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
            print('Invalid move, must be of format (0-7)(a-h)')
            self.dark_player_turn()

        print("Dark player chose", str(dark_player_turn))

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

        # Need to handle case where moving to edge of board
        for row in range(row_index-1,row_index+2):
            for column in range(column_index-1,column_index+2):
                # Only consider dark player turn for time being
                if self.board.positions[row][column] == 'l':
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

        # check clockwise from top of newly placed piece
        for opponent_piece in neighbouring_opponent_pieces:
            opponent_row_index = opponent_piece["row_index"]
            opponent_column_index = opponent_piece["column_index"]

            if (new_row_index - 1) == opponent_row_index and new_column_index == opponent_column_index:
                for row in range(new_row_index - 1):
                    if self.board.positions[row][new_column_index] == 'd':
                        return True
            elif (new_row_index - 1) == opponent_row_index and (new_column_index + 1) == opponent_column_index:
                # check for dark player piece in all rows, columns in diagonal where row < oppoent index, column > opponent indices
            elif new_row_index == opponent_row_index and (new_column_index + 1) == opponent_column_index:
                # check for dark player piece in all rows, columns in horizontal line where row == oppoent index, column > opponent indices
                pass
            elif (new_row_index + 1) == opponent_row_index and (new_column_index + 1) == opponent_column_index:
                # check for dark player piece in all rows, columns in diagonal line where row, column > opponent indices
                pass
            elif (new_row_index + 1) == opponent_row_index and new_column_index == opponent_column_index:
                # check for dark player piece in downwards vertical line all rows > opponent row indes, columns equal
                pass
            elif (new_row_index + 1) == opponent_row_index and (new_column_index - 1) == opponent_column_index:
                # check for dark player piece in downwards diagonal line all rows > opponent row indes, columns < opponent
                pass
            elif new_row_index == opponent_row_index and (new_column_index - 1) == opponent_column_index:
                # check for dark player piece in horizontal line all rows == opponent row indes, columns < opponent index
                pass
            else: 
                # check for dark player piece in all rows, columns in diagonal where row, columns < opponent indices
                pass
            
            return False

    # Valid moves in Othello
    # * Must be next to piece of other colour
    # * Must exist straight line from position of new piece to
    #   another piece of same colour

if __name__ == "__main__":
    Game()