import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from othello.game import Game

class TestStringMethods(TestCase):

    # TODO: Need to return to this
    @unittest.skip("Return to later")
    def test_initial_game(self):
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            Game()

            dark_player_prompt = "Dark player turn ..."


        self.assertEqual(fakeOutput.getvalue().rstrip(), dark_player_prompt)

    # TODO: Need to sort this out
    @unittest.skip("Return to later")
    @patch("Game.prompt_dark_player", return_value="3c")
    def test_get_user_move(self, input):
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            Game()

            dark_player_turn = "Dark player chose 3c"

        self.assertEqual(fakeOutput.getvalue().rstrip(), dark_player_prompt)



if __name__ == "__main__":
    unittest.main()