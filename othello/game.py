from math import floor
from string import ascii_lowercase

from board import Board
from messages import *
from player import Player

# TODO
# * Pass player turn if move not possible
# * Find list of possible moves
# * Handle forced moves - only one possible move
# * Check end of game - no move possible
# * Restart game
#

# Move behaviour to player class
class Game():

    def __init__(self):
        self.board = Board()
        self.players = [Player("Dark"), Player("Light")]
        self.current_player_turn = self.players[0] # reference Player instance, and below

    def player_turn(self):
        if not self.check_move_possible():
            self.current_player_turn = self.players[(self.players.index(self.current_player_turn) + 1) % 2]
            self.player_turn()

        player_prompt = self.current_player_turn.colour + " player turn ..."
        move = input(player_prompt)

        if not self.__check_move_valid(move):
            self.player_turn()

        # Refactor this
        new_row_index = int(move[0])
        new_column_index = ascii_lowercase[0:8].index(move[1])

        # Update board with player move
        self.board.positions[new_row_index][new_column_index] = self.current_player_turn.piece
        # need to clear output on previously unsuccessful attempts
        self.current_player_turn.print_player_move(move)

        # Find new scores, print current board positions
        self.calculate_player_scores()
        self.board.print()

        # Print player points after move
        for player in self.players:
            player.print_player_points()

        # Switch between players
        self.current_player_turn = self.players[(self.players.index(self.current_player_turn) + 1) % 2]
        self.player_turn()

    def calculate_player_scores(self):
        for player in self.players:
            player.points = sum(row.count(player.colour.lower()[0]) for row in self.board.positions)

    def determine_winner(self):
        dark_player = self.players[0]
        light_player = self.players[1]
        if dark_player.points > light_player.points:
            print(dark_player.colour, "player wins!")
        elif dark_player.points < light_player.points:
            print(light_player.colour, "player wins!")
        else:
            print("It's a draw!")

    def check_move_possible(self):
        # For these directions find there is an empty space in same direction
        # Abort if find piece of current player colour

        possible_moves = []

        for row_idx, row in enumerate(self.board.positions):
            for column_idx, column in enumerate(row):
                if column == self.current_player_turn.piece:
                    position = 8 * (row_idx % 8) + column_idx
                    possible_moves.append(dict([(position, [])]))

        print('possible_moves')
        print(possible_moves)
        print('--------------')
        for idx, move in enumerate(possible_moves):
            current_idx = list(move.keys())[0]
            print(current_idx)
            column_idx = current_idx % 8
            row_idx = floor(current_idx / 8)
            for row_idx in range(row_idx-1,row_idx+2):
                for column_idx in range(column_idx-1,column_idx+2):
                    try:
                        opponent_piece_colour = self.players[(self.players.index(self.current_player_turn) + 1) % 2].piece
                        print(self.board.positions[row_idx][column_idx])
                        if self.board.positions[row_idx][column_idx] == opponent_piece_colour:
                                opponent_piece = {
                                    "column_idx": column_idx,
                                    "row_idx": row_idx
                                }

                                # Refactor method row, column to num
                                # player_piece_position = 8 * (piece["row_idx"] % 8) + piece["column_idx"]
                                opponent_piece_position = 8 * (row_idx % 8) + column_idx
                                relative_position = current_idx - opponent_piece_position
                                position_to_check = opponent_piece_position - relative_position
                                while position_to_check > 0:
                                    column = position_to_check % 8
                                    row = floor(position_to_check / 8)
                                    if self.board.positions[row][column] == None:
                                        possible_moves[idx][current_idx].append({
                                            "column_idx": column,
                                            "row_idx": row
                                        })
                                        break
                                    if self.board.positions[row][column] == self.current_player_turn.piece:
                                        break
                                    position_to_check - relative_position

                    except IndexError:
                        continue
        print(possible_moves)
        self.possible_moves = possible_moves
        return len(possible_moves) > 0

    def __check_move_valid(self, move):
        return self.__check_move_format(move) and self.__check_move_legal(move)

    def __check_move_format(self, move):
        try:
            number = int(move[0])
        except ValueError:
            print(INVALID_MOVE_FORMAT)
            return False

        letter = move[1]

        if number not in range(8):
            print(INVALID_MOVE_FORMAT_FIRST_CHARACTER)
            return False

        if letter not in list(ascii_lowercase[0:8]):
            print(INVALID_MOVE_FORMAT_SECOND_CHARACTER)
            return False

        return True

    def __check_move_legal(self, move):
        if not self.__check_space_free(move):
            print(INVALID_MOVE_SPACE_OCCUPIED)
            return False

        neighbouring_opponent_pieces = self.__check_neighbouring_pieces(move)
        return neighbouring_opponent_pieces and self.__check_ending_piece(move, neighbouring_opponent_pieces)

    def __check_space_free(self, move):

        new_row_index = int(move[0])
        new_column_index = ascii_lowercase[0:8].index(move[1])

        return self.board.positions[new_row_index][new_column_index] == None

    def __check_neighbouring_pieces(self, move):

        row_index = int(move[0])
        column_index = ascii_lowercase[0:8].index(move[1]) 
        neighbouring_opponent_pieces = []

        for row in range(row_index-1,row_index+2):
            for column in range(column_index-1,column_index+2):
                try:
                    opponent_piece_colour = self.players[(self.players.index(self.current_player_turn) + 1) % 2].piece
                    if self.board.positions[row][column] == opponent_piece_colour:
                            opponent_piece = {
                                "column_index": column,
                                "row_index": row
                            }
                            neighbouring_opponent_pieces.append(opponent_piece)
                except IndexError:
                    continue

        if len(neighbouring_opponent_pieces) == 0:
            print(INVALID_MOVE_NO_NEIGHBOURING_OPPONENT_PIECE)
            return False

        return neighbouring_opponent_pieces

    # TODO: Check case of selecting 5f
    def __check_ending_piece(self, move, neighbouring_opponent_pieces):
        new_row_index = int(move[0])
        new_column_index = ascii_lowercase[0:8].index(move[1])

        new_piece_position = 8 * (new_row_index % 8) + new_column_index

        for opponent_piece in neighbouring_opponent_pieces:
            pieces_to_update = []

            opponent_row_index = opponent_piece["row_index"]
            opponent_column_index = opponent_piece["column_index"]
            pieces_to_update.append({
                "column": opponent_column_index,
                "row": opponent_row_index
            })

            opponent_piece_position = 8 * (opponent_row_index % 8) + opponent_column_index
            relative_position = new_piece_position - opponent_piece_position
            position_to_check = opponent_piece_position - relative_position
            while position_to_check > 0:
                column = position_to_check % 8
                row = floor(position_to_check / 8)
                piece_to_update = {
                    "column": column,
                    "row": row
                }
                pieces_to_update.append(piece_to_update)
                if self.board.positions[row][column] == self.current_player_turn.piece:
                    self.__update_board_pieces(pieces_to_update)
                    return True
                elif self.board.positions[row][column] == None:
                    print(INVALID_MOVE_SPACES_BETWEEN_PIECES)
                    return False
                position_to_check - relative_position
            
            print(INVALID_MOVE_NOT_ENCLOSING_PIECE)
            return False

    def __update_board_pieces(self, pieces):
        for piece in pieces:
            column = piece["column"]
            row = piece["row"]
            self.board.positions[row][column] = self.current_player_turn.piece

if __name__ == "__main__":
    game = Game()
    # game.player_turn()
    game.check_move_possible()