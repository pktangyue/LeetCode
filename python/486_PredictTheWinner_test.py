import unittest


class TestSolution(unittest.TestCase):

    def test_PredictTheWinner(self):
        Solution = __import__('486_PredictTheWinner').Solution
        self.assertEqual(
            False,
            Solution().PredictTheWinner([1, 5, 2])
        )
        self.assertEqual(
            True,
            Solution().PredictTheWinner([1, 5, 233, 7])
        )
        self.assertEqual(
            True,
            Solution().PredictTheWinner([1, 5, 2, 4, 6])
        )
