# Refactor player behaviour here

class Player():

    def __init__(self, colour):
        self.colour = colour
        self.piece = "d" if self.colour == "Dark" else "l"
        self.points = 0

    def print_player_move(self, move):
        print(self.colour + " player chose " + str(move), "\n")

    def print_player_points(self):
        print(self.colour, "player has", self.points, "points", "\n")