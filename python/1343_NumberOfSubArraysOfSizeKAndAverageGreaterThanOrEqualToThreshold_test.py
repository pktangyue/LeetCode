import unittest


class TestSolution(unittest.TestCase):

    def test_NumOfSubarrays(self):
        Solution = __import__('1343_NumberOfSubArraysOfSizeKAndAverageGreaterThanOrEqualToThreshold').Solution
        self.assertEqual(
            3,
            Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
        )
        self.assertEqual(
            5,
            Solution().numOfSubarrays([1, 1, 1, 1, 1], 1, 0)
        )
        self.assertEqual(
            6,
            Solution().numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5)
        )
        self.assertEqual(
            1,
            Solution().numOfSubarrays([7, 7, 7, 7, 7, 7, 7], 7, 7)
        )
        self.assertEqual(
            1,
            Solution().numOfSubarrays([4, 4, 4, 4], 4, 1)
        )
