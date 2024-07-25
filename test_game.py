import unittest
from game import create_board, place_input_on_board, is_full, check_winner

class TestTicTacToe(unittest.TestCase):

    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), 3)
        self.assertTrue(all(len(row) == 3 for row in board))
        self.assertTrue(all(cell == ' ' for row in board for cell in row))

    def test_place_input_on_board(self):
        board = create_board()
        self.assertTrue(place_input_on_board(board, 0, 0, 'X'))
        self.assertEqual(board[0][0], 'X')
        self.assertFalse(place_input_on_board(board, 0, 0, 'O'))
        self.assertEqual(board[0][0], 'X')

    def test_is_full(self):
        board = create_board()
        self.assertFalse(is_full(board))
        for row in range(3):
            for col in range(3):
                board[row][col] = 'X'
        self.assertTrue(is_full(board))

    def test_check_winner(self):
        board = create_board()
        # Test horizontal win
        board[0] = ['X', 'X', 'X']
        self.assertTrue(check_winner(board, 'X'))
        # Test vertical win
        board = create_board()
        for row in range(3):
            board[row][0] = 'X'
        self.assertTrue(check_winner(board, 'X'))
        # Test diagonal win
        board = create_board()
        for i in range(3):
            board[i][i] = 'X'
        self.assertTrue(check_winner(board, 'X'))
        # Test no win
        board = create_board()
        self.assertFalse(check_winner(board, 'X'))

if __name__ == '__main__':
    unittest.main()