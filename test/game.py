import unittest
from unittest.mock import patch
from io import StringIO

from othello.game import Game

class TestStringMethods(unittest.TestCase):

    def test_initial_game(self):
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            Game()

            dark_player_prompt = "Dark player turn ..."


        self.assertEqual(fakeOutput.getvalue().rstrip(), dark_player_prompt)

if __name__ == '__main__':
    unittest.main()