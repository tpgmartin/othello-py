import sys

class Board():

    def __init__(self):
        self.positions = []

        for i in range(8):
            self.positions.append([None] * 8)

        self.positions[3][3] = "l"
        self.positions[3][4] = "d"
        self.positions[4][3] = "d"
        self.positions[4][4] = "l"
    
    def print(self):
        formatted_board = self.__format_board()
        print(formatted_board)

    def __format_board(self):

        formatted_board = ""

        for row in range(len(self.positions)):
            new_row = (
                str(self.__format_position(self.positions[row][0])) + "|" +
                str(self.__format_position(self.positions[row][1])) + "|" +
                str(self.__format_position(self.positions[row][2])) + "|" +
                str(self.__format_position(self.positions[row][3])) + "|" +
                str(self.__format_position(self.positions[row][4])) + "|" +
                str(self.__format_position(self.positions[row][5])) + "|" +
                str(self.__format_position(self.positions[row][6])) + "|" +
                str(self.__format_position(self.positions[row][7]))
            )
            if row != len(self.positions)-1:
                new_row += "\n_ _ _ _ _ _ _ _\n"

            formatted_board += new_row

        return formatted_board

    def __format_position(self, position):
        return " " if position == None else position
