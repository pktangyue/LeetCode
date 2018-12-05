import unittest


class TestSolution(unittest.TestCase):

    def test_ValidTicTacToe(self):
        Solution = __import__('794_ValidTicTacToeState').Solution
        self.assertEqual(
            False,
            Solution().validTicTacToe(["O  ", "   ", "   "])
        )
        self.assertEqual(
            False,
            Solution().validTicTacToe(["XOX", " X ", "   "])
        )
        self.assertEqual(
            False,
            Solution().validTicTacToe(["XXX", "   ", "OOO"])
        )
        self.assertEqual(
            True,
            Solution().validTicTacToe(["XOX", "O O", "XOX"])
        )
        self.assertEqual(
            True,
            Solution().validTicTacToe(["XXX", "OOX", "OOX"])
        )
        self.assertEqual(
            False,
            Solution().validTicTacToe(["XXX", "XOO", "OO "])
        )
