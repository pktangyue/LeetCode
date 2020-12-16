import unittest


class TestSolution(unittest.TestCase):

    def test_MinSubsequence(self):
        Solution = __import__('1403_MinimumSubsequenceInNonIncreasingOrder').Solution
        self.assertEqual(
            [10, 9],
            Solution().minSubsequence([4, 3, 10, 9, 8]),
        )
        self.assertEqual(
            [7, 7, 6],
            Solution().minSubsequence([4, 4, 7, 6, 7]),
        )
        self.assertEqual(
            [6],
            Solution().minSubsequence([6]),
        )
