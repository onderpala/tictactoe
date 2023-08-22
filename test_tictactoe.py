import unittest

from io import StringIO

from contextlib import redirect_stdout

from tictactoe import Game

class TestPlayerWon(unittest.TestCase):
    def setUp(self):
        self.game = Game()


    def test_valid_player(self):
        self.assertTrue(self.game.player_won('P1'))

    def test_invalid_player(self):
        self.assertFalse(self.game.player_won('P4'))

    def test_stdout_with_valid_player(self):
        output = 'P1 Wins!!!\n'
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.game.player_won('P1')
        system_output = buffer.getvalue()
        self.assertEqual(system_output, output)
        
        

class TestCheckWon(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.horizontal_win = [ # P1 wins
            ['X', 'X', 'X'],
            ['O', 'O', 6],
            [7, 8, 9]
        ]
        self.vertical_win = [ # P2 wins
            ['O', 'X', 'X'],
            ['O', 'O', 6],
            ['O', 'X', 'X']
        ]
        self.diagonal_win = [ # P1 wins
            ['X', 2, 'O'],
            ['O', 'X', 6],
            [7, 8, 'X']
        ]
        self.no_win = [ # Noone wins
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

    def test_horizontal_win_with_winner(self):
        self.game.board = self.horizontal_win
        self.assertTrue(self.game.check_won('P1'))

    def test_horizontal_win_with_loser(self):
        self.game.board = self.horizontal_win
        self.assertFalse(self.game.check_won('P2'))

    def test_vertical_win_with_winner(self):
        self.game.board = self.vertical_win
        self.assertTrue(self.game.check_won('P2'))

    def test_vertical_win_with_loser(self):
        self.game.board = self.vertical_win
        self.assertFalse(self.game.check_won('P1'))

    def test_diagonal_win_with_winner(self):
        self.game.board = self.diagonal_win
        self.assertTrue(self.game.check_won('P1'))

    def test_diagonal_win_with_loser(self):
        self.game.board = self.diagonal_win
        self.assertFalse(self.game.check_won('P2'))

    def test_no_win(self):
        self.game.board = self.no_win
        self.assertFalse(self.game.check_won('P1'))
        self.assertFalse(self.game.check_won('P2'))


class TestDisplayGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_stdout(self):
        output = '1 2 3 \n4 5 6 \n7 8 9 \n'
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.game.display_game()
        system_output =  buffer.getvalue()
        self.assertEqual(system_output, output)

class TestDisplayCoordinate(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_right_coordinate(self):
        coordinate = {'x': 0, 'y': 0}
        self.assertEqual(self.game.display_coordinate(coordinate), 1)
        
    def test_no_coordinate(self):
        coordinate = {}
        self.assertFalse(self.game.display_coordinate(coordinate))

    def test_with_nonexistent_coordinate(self):
        coordinate = {'x': 3, 'y': 3}
        self.assertFalse(self.game.display_coordinate(coordinate))

    
class TestGetCoordinate(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.coordinates = {'1': [0, 0],
                       '2': [1, 0],
                       '3': [2, 0],
                       '4': [0, 1],
                       '5': [1, 1],
                       '6': [2, 1],
                       '7': [0, 2],
                       '8': [1, 2],
                       '9': [2, 2]}

    def test_wrong_place(self):
        self.assertFalse(self.game.get_coordinate('12'))

    def test_invalid_input(self):
        self.assertFalse(self.game.get_coordinate('a'))

    def test_every_place_returns_right_coordinates(self):
        for coordinate in self.coordinates:
            self.assertEqual(
                self.game.get_coordinate(coordinate),
                    {
                    'x': self.coordinates[coordinate][0],
                    'y': self.coordinates[coordinate][1]
                    }
                )
            
class TestPlace(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.starting_board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        self.expected_board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    def test_successful_place_with_Player1(self):
        self.game.place('P1', 1)
        self.expected_board[0][0] = 'X'
        self.assertEqual(self.game.board, self.expected_board)
    def test_successful_place_with_Player2(self):
        self.expected_board[0][0] = 'O'
        self.game.place('P2', 1)
        self.assertEqual(self.game.board, self.expected_board)

    def test_place_for_occupied_place(self):
        self.game.board[0][0] = 'X'
        self.expected_board[0][0] = 'X'
        self.assertFalse(self.game.place('P1', 1))
        self.assertEqual(self.game.board, self.expected_board)
        self.assertFalse(self.game.place('P2', 1))
        self.assertEqual(self.game.board, self.expected_board)

    def test_wrong_place(self):
        self.assertFalse(self.game.place('P1', 11))
        self.assertEqual(self.game.board, self.starting_board)
        self.assertFalse(self.game.place('P1', 0))
        self.assertEqual(self.game.board, self.starting_board)
        self.game.place('P1', 'X')
        self.assertEqual(self.game.board, self.starting_board)
    
    def test_wrong_player(self):
        self.assertFalse(self.game.place('A1', 1))
        self.assertEqual(self.game.board, self.starting_board)





if __name__ == '__main__':
    unittest.main()