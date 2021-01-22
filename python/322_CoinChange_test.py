import unittest


class TestSolution(unittest.TestCase):

    def test_coinChange(self):
        Solution = __import__('322_CoinChange').Solution
        self.assertEqual(
            20,
            Solution().coinChange(coins=[186, 419, 83, 408], amount=6249)
        )
        self.assertEqual(
            20,
            Solution().coinChange(coins=[1, 2, 5], amount=100)
        )
        self.assertEqual(
            3,
            Solution().coinChange(coins=[1, 2, 5], amount=11)
        )
        self.assertEqual(
            -1,
            Solution().coinChange(coins=[2], amount=3)
        )
        self.assertEqual(
            0,
            Solution().coinChange(coins=[1], amount=0)
        )
        self.assertEqual(
            1,
            Solution().coinChange(coins=[1], amount=1)
        )
        self.assertEqual(
            2,
            Solution().coinChange(coins=[1], amount=2)
        )
