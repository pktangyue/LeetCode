import unittest


class TestSolution(unittest.TestCase):

    def test_change(self):
        Solution = __import__('518_CoinChange2').Solution
        self.assertEqual(
            4,
            Solution().change(amount=5, coins=[1, 2, 5])
        )
        self.assertEqual(
            0,
            Solution().change(amount=3, coins=[2])
        )
        self.assertEqual(
            1,
            Solution().change(amount=10, coins=[10])
        )
