import unittest


class TestSolution(unittest.TestCase):

    def test_FindNumberOfLIS(self):
        Solution = __import__('673_NumberOfLongestIncreasingSubsequence').Solution
        self.assertEqual(
            3,
            Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]),
        )
        self.assertEqual(
            1,
            Solution().findNumberOfLIS([3, 1, 2])
        )
        self.assertEqual(
            2,
            Solution().findNumberOfLIS([1, 3, 5, 4, 7])
        )
        self.assertEqual(
            5,
            Solution().findNumberOfLIS([2, 2, 2, 2, 2])
        )
