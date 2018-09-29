# Refactor player behaviour here

class Player():

    def __init__(self, colour):
        self.colour = colour
        self.piece = "d" if self.colour == "Dark" else "l"
        self.points = 0