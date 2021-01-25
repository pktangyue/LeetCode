import unittest


class TestSolution(unittest.TestCase):

    def test_maxCoins(self):
        Solution = __import__('1561_MaximumNumberOfCoinsYouCanGet').Solution
        self.assertEqual(
            9,
            Solution().maxCoins(piles=[2, 4, 1, 2, 7, 8])
        )
