"""
    Game flow for two human players only

    1. Render board
    2. Initialise new game - place four counters in middle of board
    3. Prompt dark player for move
    4. Show legal moves - if no moves available to player skip to 8.
    5. Allow legal move
    6. Apply colour changes to pieces 
    7. Calculate score
    8. Check if game finished, if yes go to 14. otherwise continue
    8. Prompt light player for move
    9. Show legal moves - if no moves available to player skip to 13.
    10. Allow legal move
    11. Apply colour changes to pieces 
    12. Calculate score
    13. Check if game finished, if yes go to 14. otherwise go to 3.
    14. Game ends, declare winner, return to 1.
"""
