import unittest
from unittest.mock import patch
from io import StringIO

from othello.board import Board

class TestStringMethods(unittest.TestCase):

    def test_initial_board(self):
        board = Board()

        self.assertEqual(len(board.positions), 8)
        self.assertEqual(len(board.positions[0]), 8)
        self.assertEqual(board.positions[3][3], "l")
        self.assertEqual(board.positions[3][4], "d")
        self.assertEqual(board.positions[4][3], "d")
        self.assertEqual(board.positions[4][4], "l")
    
    def test_print_board(self):
        board = Board()

        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            board.print()

            formatted_board = (
                " | | | | | | | \n" +
                "_ _ _ _ _ _ _ _\n" +
                " | | | | | | | \n" +
                "_ _ _ _ _ _ _ _\n" +
                " | | | | | | | \n" +
                "_ _ _ _ _ _ _ _\n" +
                " | | |l|d| | | \n" +
                "_ _ _ _ _ _ _ _\n" +
                " | | |d|l| | | \n" +
                "_ _ _ _ _ _ _ _\n" +
                " | | | | | | | \n" +
                "_ _ _ _ _ _ _ _\n" +
                " | | | | | | | \n" +
                "_ _ _ _ _ _ _ _\n" +
                " | | | | | | |"
            )

            self.assertEqual(fakeOutput.getvalue().rstrip(), formatted_board)

if __name__ == "__main__":
    unittest.main()