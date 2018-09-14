"""
    Game flow for two human players only

    1. Render board
    2. Initialise new game - place four counters in middle of board
    3. Prompt dark player for move
    4. Show legal moves - if no moves available to player skip to 7.
    5. Allow legal move
    6. Apply colour changes to pieces 
    7. Check if game finished, if yes go to 13. otherwise continue
    8. Prompt light player for move
    9. Show legal moves - if no moves available to player skip to 13.
    10. Allow legal move
    11. Apply colour changes to pieces 
    12. Check if game finished, if yes go to 13. otherwise go to 3.
    13. Game ends, declare winner, return to 1.
"""

class Board():

    def __init__(self):
        pass