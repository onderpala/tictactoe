import unittest

from io import StringIO

from contextlib import redirect_stdout

from tictactoe import Game




class TestTictactoe(unittest.TestCase):

    def setUp(self):
        self.game = Game()
    

    def test_player_won(self):
        """
        Conditions:
            player is not valid returns False
            player is valid returns True
            test stdout (Optional)
        """

        self.assertTrue(self.game.player_won('P1'))
        self.assertFalse(self.game.player_won('P4'))

        output = 'P1 Wins!!!\n'
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.game.player_won('P1')
        system_output = buffer.getvalue()
        self.assertEqual(system_output, output)

    
    def test_check_won(self):
        """
        Conditions:
            test horizontal win
            test vertical win
            test diagonal win
            test no win returns False for every player
            
        """
        horizontal_win = [ # P1 wins
            ['X', 'X', 'X'],
            ['O', 'O', 6],
            [7, 8, 9]
        ]
        vertical_win = [ # P2 wins
            ['O', 'X', 'X'],
            ['O', 'O', 6],
            ['O', 'X', 'X']
        ]
        diagonal_win = [ # P1 wins
            ['X', 2, 'O'],
            ['O', 'X', 6],
            [7, 8, 'X']
        ]
        no_win = [ # Noone wins
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        self.game.board = horizontal_win
        self.assertTrue(self.game.check_won('P1'))
        self.assertFalse(self.game.check_won('P2'))

        self.game.board = vertical_win
        self.assertTrue(self.game.check_won('P2'))
        self.assertFalse(self.game.check_won('P1'))

        self.game.board = diagonal_win
        self.assertTrue(self.game.check_won('P1'))
        self.assertFalse(self.game.check_won('P2'))

        self.game.board = no_win
        self.assertFalse(self.game.check_won('P1'))
        self.assertFalse(self.game.check_won('P2'))


    def test_display_game(self):
        """
        Conditions:
            test stdout is right
        
        """
        output = '1 2 3 \n4 5 6 \n7 8 9 \n'
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.game.display_game()
        system_output =  buffer.getvalue()
        self.assertEqual(system_output, output)

        
    def test_display_coordinate(self):
        """
        Description:
            Test display_coordinate function

        Conditions:
            right coordinates
            there is no x or y in coordinate
            wrong coordinates
        """
        coordinate = {'x': 0, 'y': 0}
        word = 1
        self.assertEqual(self.game.display_coordinate(coordinate), word)

        coordinate = {}
        self.assertFalse(self.game.display_coordinate(coordinate))

        coordinate = {'x': 3, 'y': 3}
        self.assertFalse(self.game.display_coordinate(coordinate))

    

    def test_get_coordinate(self):
        """
        Conditions:
            test place is wrong int return False ex: '12'
            test place is str as real str return False ex: 'a'
            test every place right return coordinate
        """

        self.assertFalse(self.game.get_coordinate('12'))
        self.assertFalse(self.game.get_coordinate('a'))



        #place variable is string bec inputs always str
        coordinates = {'1': [0, 0],
                       '2': [1, 0],
                       '3': [2, 0],
                       '4': [0, 1],
                       '5': [1, 1],
                       '6': [2, 1],
                       '7': [0, 2],
                       '8': [1, 2],
                       '9': [2, 2]}
        for coordinate in coordinates:
            cr = self.game.get_coordinate(coordinate)
            self.assertEqual(cr, {'x': coordinates[coordinate][0], 'y': coordinates[coordinate][1]})

    def test_place(self):
        starting_board = [[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]
        expected_board = [[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]
        
        # Test successful P1
        self.game.place('P1', 1)
        print(self.game.board)
        expected_board[0][0] = 'X'
        self.assertEqual(self.game.board, expected_board) # Assert only chosen place effected
        self.game.board = starting_board
        
        # Test successful P2
        expected_board[0][0] = 'O'
        self.game.place('P2', 1)
        self.assertEqual(self.game.board, expected_board) # Assert only chosen place effected

        # Test occupied place
        self.game.place('P1', 1) # As opponent
        self.assertEqual(self.game.board, expected_board)
        self.game.place('P2', 1) # As itself
        self.assertEqual(self.game.board, expected_board)

        # Test wrong int
        self.game.board = starting_board
        self.game.place('P1', 11)
        self.assertEqual(self.game.board, starting_board)
        self.game.board = starting_board

        self.game.place('P1', 0)
        self.assertEqual(self.game.board, starting_board)
        self.game.board = starting_board

        # Test wrong Player
        self.game.place('A1', 1)
        self.assertEqual(self.game.board, starting_board)
        self.game.board = starting_board
        
        # Test place as a string
        self.game.place('P1', 'X')
        self.assertEqual(self.game.board, starting_board)





if __name__ == '__main__':
    unittest.main()