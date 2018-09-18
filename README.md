# Othello Py

An implementation of the game [Othello](https://en.wikipedia.org/wiki/Reversi) in Python

# Game Play

## For Two Human Players Only

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

# TODO

* Create board
* Create pieces
* Render initial board position
* ...

# Reference Board

"0a|0b|0c|0d|0e|0f|0g|0h\n"
"_ _ _ _ _ _ _ _\n"
"1a|1b|1c|1d|1e|1f|1g|1h\n"
"_ _ _ _ _ _ _ _\n"
"2a|2b|2c|2d|2e|2f|2g|2h\n"
"_ _ _ _ _ _ _ _\n"
"3a|3b|3c|3d|3e|3f|3g|3h\n"
"_ _ _ _ _ _ _ _\n"
"4a|4b|4c|4d|4e|4f|4g|4h\n"
"_ _ _ _ _ _ _ _\n"
"5a|5b|5c|5d|5e|5f|5g|5h\n"
"_ _ _ _ _ _ _ _\n"
"6a|6b|6c|6d|6e|6f|6g|6h\n"
"_ _ _ _ _ _ _ _\n"
"7a|7b|7c|7d|7e|7f|7g|7h"