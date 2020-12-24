import unittest


class TestSolution(unittest.TestCase):

    def test_LengthOfLongestSubstring(self):
        Solution = __import__('910_SmallestRangeII').Solution
        self.assertEqual(
            0,
            Solution().smallestRangeII([1], 0)
        )
        self.assertEqual(
            6,
            Solution().smallestRangeII([0, 10], 2)
        )
        self.assertEqual(
            3,
            Solution().smallestRangeII([1, 3, 6], 3)
        )
