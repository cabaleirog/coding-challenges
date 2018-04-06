import unittest

from hacker_rank.ways_to_give_a_check import CheckGame


class TestGame(unittest.TestCase):

    def setUp(self):
        self.size = 8
        self.game = CheckGame()
        board = _empty_board(self.size)
        self.game.set_board(board)

    def test_bishop_movement_top_left_corner(self):
        row, col = (0, 0)
        rdown, rup, ldown, lup = self.game.bishop_movement(row, col)
        self.assertEqual(rdown, [(x, x) for x in range(1, self.size)])
        self.assertEqual(rup, [])
        self.assertEqual(ldown, [])
        self.assertEqual(lup, [])

    def test_bishop_movement_bottom_left_corner(self):
        row, col = (self.size - 1, 0)
        rdown, rup, ldown, lup = self.game.bishop_movement(row, col)
        self.assertEqual(rdown, [])
        self.assertEqual(rup, [(row - x - 1, x + 1) for x in range(row)])
        self.assertEqual(ldown, [])
        self.assertEqual(lup, [])

    def test_bishop_movement_bottom_right_corner(self):
        row, col = (self.size - 1, self.size - 1)
        rdown, rup, ldown, lup = self.game.bishop_movement(row, col)
        self.assertEqual(rdown, [])
        self.assertEqual(rup, [])
        self.assertEqual(ldown, [])
        self.assertEqual(lup, [(row - x - 1, col - x - 1) for x in range(row)])

    def test_bishop_movement_top_right_corner(self):
        row, col = (0, self.size - 1)
        rdown, rup, ldown, lup = self.game.bishop_movement(row, col)
        self.assertEqual(rdown, [])
        self.assertEqual(rup, [])
        self.assertEqual(ldown, [(x + 1, col - x - 1) for x in range(col)])
        self.assertEqual(lup, [])


class TestTotalWaysToGiveACheck(unittest.TestCase):

    def setUp(self):
        self.size = 8
        self.game = CheckGame()
        self.board = _empty_board(self.size)

    def test_game_one(self):
        self.board[1][1] = 'k'
        self.board[1][3] = 'P'
        self.board[6][1] = 'K'
        self.game.set_board(self.board)
        self.assertEqual(self.game.ways_to_give_a_check(), 1)

    def test_game_two(self):
        self.board[1][6] = 'P'
        self.board[2][4] = 'k'
        self.board[6][4] = 'K'
        self.game.set_board(self.board)
        self.assertEqual(self.game.ways_to_give_a_check(), 2)

    def test_game_three(self):
        self.board[1][2] = 'P'
        self.board[7][1] = 'K'
        self.board[1][4] = 'k'
        self.game.set_board(self.board)
        self.assertEqual(self.game.ways_to_give_a_check(), 1)

    def test_game_four(self):
        self.board[1][0] = 'P'
        self.board[6][0] = 'Q'
        self.board[7][1] = 'K'
        self.board[1][1] = 'q'
        self.board[2][1] = 'k'
        self.game.set_board(self.board)
        self.assertEqual(self.game.ways_to_give_a_check(), 1)

    def test_game_five(self):
        self.board[1][1] = 'P'
        self.board[7][1] = 'K'
        self.board[2][0] = 'k'
        self.game.set_board(self.board)
        self.assertEqual(self.game.ways_to_give_a_check(), 1)

    def test_game_six(self):
        self.board[1][7] = 'P'
        self.board[7][1] = 'K'
        self.board[1][5] = 'k'
        self.game.set_board(self.board)
        self.assertEqual(self.game.ways_to_give_a_check(), 1)

    def test_game_seven(self):
        self.board[1][2] = 'P'
        self.board[7][1] = 'K'
        self.board[2][0] = 'k'
        self.game.set_board(self.board)
        self.assertEqual(self.game.ways_to_give_a_check(), 2)


def _empty_board(board_size=8):
    return [['#'] * board_size for _ in range(board_size)]


if __name__ == '__main__':
    unittest.main()
