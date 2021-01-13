import unittest


class TestSolution(unittest.TestCase):

    def test_smallestDistancePair(self):
        Solution = __import__('719_FindKthSmallestPairDistance').Solution
        self.assertEqual(
            0,
            Solution().smallestDistancePair(nums=[1, 3, 1], k=1)
        )
        self.assertEqual(
            1,
            Solution().smallestDistancePair(
                [1, 2, 0, 2, 1, 0, 1, 1, 0, 2, 2, 0, 2, 0, 1, 1, 1, 0, 1, 0, 1, 1, 2, 2, 2, 2, 0, 0, 2, 1, 2, 1, 2, 0,
                 0, 0, 1, 0, 0, 1, 0, 2, 1, 1, 1, 1, 0, 2, 2, 1, 0, 2, 0, 2, 2, 2, 1, 0, 2, 2, 2, 2, 0, 0, 1, 0, 1, 1,
                 2, 1, 2, 2, 1, 1, 0, 2, 0, 1, 0, 1, 1, 2, 0, 1, 1, 1, 1, 2, 0, 2, 2, 0, 0, 1, 1, 1, 1, 2, 1, 2, 2, 1,
                 2, 0, 1, 2, 2, 1, 1, 2, 1, 0, 1, 1, 1, 0, 0, 1, 2, 0, 2, 1, 0, 1, 2, 0, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0,
                 1, 0, 1, 0, 1, 2, 2, 2, 0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 1, 1, 2, 0,
                 2, 1, 2, 0, 0, 1, 0, 1, 2, 1, 0, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 0, 0, 0, 0, 1, 2, 2, 1, 1, 0, 1, 2, 0,
                 0, 2, 1, 2, 1, 2, 0, 2, 1, 1, 2, 2, 2, 2, 2, 0, 1, 1, 0, 1, 2, 2, 0, 2, 2, 2, 0, 2, 0, 1, 1, 2, 2, 0,
                 2, 2, 2, 2, 2, 2, 1, 0, 2, 2, 2, 0, 2, 0, 2, 0, 2, 1, 0, 1, 0, 1, 1, 0, 2, 0, 1, 0, 0, 2, 0, 0, 0, 2,
                 0, 2, 2, 0, 2, 0, 0, 1, 1, 0, 2, 0, 1, 2, 2, 0, 1, 1, 2, 0, 0, 0, 2, 1, 0, 1, 0, 2, 1, 2, 0, 1, 2, 1,
                 1, 1, 0, 1, 2, 1, 2, 2, 1, 2, 0, 2, 1, 0, 1, 1, 1, 2, 0, 2, 2, 2, 2, 1, 0, 2, 2, 1, 1, 1, 1, 0, 1, 2,
                 2, 0, 1, 2, 2, 1, 0, 0, 1, 2, 1, 0, 2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 2, 0, 2, 0, 1, 2, 2, 0, 2, 1, 2,
                 2, 0, 0, 0, 0, 2, 1, 1, 2, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 0, 2, 1, 2, 0, 1, 2, 1, 2, 1, 0, 1, 0, 1, 0,
                 0, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 0, 1, 1, 2, 2, 1, 2, 2, 2, 1, 0, 1, 1, 1, 0, 0, 0, 2, 1, 1, 1, 2, 2,
                 1, 2, 0, 2, 1, 2, 0, 2, 2, 2, 1, 1, 2, 2, 0, 0, 2, 2, 2, 1, 2, 2, 1, 0, 2, 0, 2, 0, 2, 1, 2, 2, 1, 1,
                 1, 1, 1, 0, 0, 1, 0, 2, 2, 0, 0, 2, 1, 0, 1, 0, 2, 1, 0, 0, 0, 0, 1, 2, 1, 2, 0, 0, 1, 1, 2, 2, 2, 2,
                 0, 2, 1, 0, 0, 0, 2, 0, 1, 1, 0, 2, 1, 1, 1, 2, 1, 0, 0, 1, 0, 1, 0, 1, 2, 0, 2, 1, 0, 0, 1, 2, 1, 1,
                 0, 0, 0, 2, 2, 2, 1, 1, 2, 2, 0, 1, 0, 2, 2, 2, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 2, 0, 2,
                 0, 2, 1, 2, 2, 2, 0, 1, 0, 1, 2, 0, 2, 2, 1, 2, 0, 1, 2, 2, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0,
                 2, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 2, 2, 0, 2, 2,
                 0, 0, 1, 2, 0, 1, 1, 1, 2, 0, 0, 0, 2, 0, 2, 2, 2, 2, 1, 0, 2, 2, 0, 0, 1, 1, 2, 2, 2, 1, 1, 2, 0, 1,
                 0, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 1, 1, 1, 2, 0, 1, 0, 1, 2, 2, 0, 0, 2, 0, 1, 2, 1, 2, 1, 0, 0, 1, 0,
                 0, 1, 2, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 2, 1, 1, 0, 0, 2,
                 2, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 2, 0, 1, 1, 2, 2, 1, 1, 0, 2, 0, 0, 1, 0, 1, 2, 2, 1, 2, 2, 2, 2, 2,
                 1, 2, 0, 0, 0, 1, 1, 0, 0, 2, 1, 0, 1, 0, 2, 2, 0, 1, 2, 2, 2, 0, 0, 0, 2, 2, 1, 2, 1, 0, 0, 0, 1, 1,
                 2, 1, 2, 0, 1, 2, 1, 0, 1, 2, 0, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 0, 1, 0, 2, 1, 2, 0, 2, 0, 0, 0, 1, 2,
                 1, 0, 0, 0, 1, 2, 0, 2, 2, 2, 1, 0, 2, 2, 1, 1, 2, 0, 0, 1, 2, 2, 2, 1, 2, 1, 2, 1, 0, 2, 2, 0, 0, 0,
                 2, 0, 1, 0, 1, 0, 2, 2, 2, 2, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 2, 0, 1, 0, 0, 2, 0, 1, 1, 1, 1, 2, 0, 1,
                 1, 2, 0, 2, 1, 2, 1, 1, 0, 1, 1, 2, 1, 2, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 2, 0, 0, 1, 0, 1, 2, 2, 1, 2,
                 0, 2, 2, 2, 0, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 0, 2, 1, 2, 1, 1, 0, 2, 1, 2, 0, 1, 1,
                 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 2, 2, 1, 1, 0, 1, 0, 0, 0, 2, 2, 2, 0, 1, 2, 1, 2, 0, 2, 1, 0,
                 0, 1, 2, 2, 1, 0, 1, 2, 0, 0, 2, 1, 1, 2, 0, 0, 1, 0, 2, 2, 2, 2, 0, 1, 0, 0, 0, 1, 1, 0, 2, 0, 2, 0,
                 2, 2, 2, 0, 2, 0, 0, 2, 1, 0, 2, 2, 2, 1, 2, 0, 2, 2, 0, 2, 1, 2, 2, 0, 1, 0, 2, 0, 1, 1, 2, 2, 2, 2,
                 0, 0, 0, 0, 2, 2, 2, 2, 1, 0, 2, 0, 2, 0, 1, 0, 1, 1, 2, 2, 1, 2, 1, 2, 0, 1, 2, 2, 2, 0, 1, 0, 1, 0,
                 1, 0, 1, 0, 1, 2, 2, 0, 2, 2, 2, 0, 1, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 2, 0, 0, 2, 2, 2, 2,
                 1, 2, 2, 1, 2, 0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2, 0, 1, 0, 2,
                 2, 2, 0, 1, 0, 2, 1, 2, 2, 0, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 1, 2, 1, 1, 0, 0, 1, 0, 2, 0, 2, 2, 2,
                 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 0, 1, 2, 2, 0, 0, 2, 1, 0, 2, 1, 0, 2, 2, 0, 2, 1, 0, 2, 1, 0, 0,
                 0, 0, 2, 0, 1, 0, 2, 0, 1, 2, 2, 0, 1, 0, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 0, 1, 2, 2, 1,
                 2, 2, 0, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 0, 0, 2, 0, 2, 0, 1, 1, 0, 0, 2, 1, 0, 0,
                 1, 2, 0, 1, 0, 2, 1, 1, 1, 1, 2, 2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 2, 0, 1, 0, 2, 0, 2, 2, 2, 1, 2, 2, 0,
                 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 2, 1, 2, 1, 2, 2, 1, 1, 0, 2, 1, 0, 0,
                 1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 2, 0, 0, 2, 1, 1, 2, 2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 2, 1, 1, 0, 0, 0, 1,
                 1, 1, 0, 0, 1, 1, 1, 2, 2, 1, 2, 1, 0, 2, 0, 1, 0, 0, 2, 0, 0, 0, 2, 1, 0, 2, 0, 2, 1, 1, 2, 0, 1, 1,
                 0, 2, 0, 1, 2, 2, 0, 0, 2, 0, 1, 1, 0, 2, 2, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 2, 2, 1, 0, 1, 2, 2,
                 2, 2, 1, 1, 2, 2, 2, 0, 1, 2, 0, 2, 1, 2, 1, 0, 2, 0, 1, 0, 0, 2, 1, 0, 0, 0, 2, 0, 0, 1, 2, 2, 0, 0,
                 1, 0, 1, 1, 2, 2, 2, 0, 2, 1, 0, 2, 0, 1, 2, 1, 0, 1, 1, 1, 2, 1, 0, 0, 0, 2, 1, 0, 2, 2, 0, 1, 0, 2,
                 0, 2, 2, 2, 0, 1, 2, 2, 2, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 2, 2, 2, 0, 1, 0, 0, 1, 2, 2, 2, 0, 1, 1,
                 1, 2, 0, 2, 1, 1, 2, 2, 1, 0, 1, 2, 0, 2, 1, 1, 0, 1, 1, 2, 0, 1, 0, 2, 1, 2, 0, 2, 2, 2, 2, 0, 2, 0,
                 2, 1, 0, 1, 0, 2, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 2, 1, 2, 0, 0, 0,
                 2, 2, 2, 2, 1, 1, 1, 0, 1, 2, 2, 0, 0, 1, 1, 0, 2, 0, 2, 1, 2, 0, 0, 2, 1, 0, 0, 0, 2, 2, 0, 1, 1, 0,
                 0, 0, 0, 1, 0, 1, 1, 2, 1, 2, 1, 2, 0, 1, 1, 2, 0, 0, 2, 1, 0, 0, 2, 0, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2,
                 0, 1, 2, 0, 1, 2, 1, 2, 0, 2, 1, 0, 2, 1, 1, 2, 0, 2, 0, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 0,
                 1, 1, 1, 2, 0, 1, 2, 1, 1, 0, 2, 1, 0, 2, 0, 0, 0, 2, 1, 0, 1, 2, 0, 1, 0, 1, 1, 0, 0, 1, 0, 2, 0, 0,
                 0, 0, 2, 2, 0, 1, 1, 2, 1, 2, 2, 1, 0, 1, 1, 2, 2, 0, 1, 0, 1, 0, 2, 1, 0, 2, 0, 2, 2, 1, 1, 1, 1, 2,
                 2, 2, 2, 0, 1, 1, 0, 2, 0, 1, 2, 1, 2, 0, 0, 2, 2, 1, 2, 2, 1, 1, 0, 0, 0, 0, 2, 1, 0, 2, 2, 0, 1, 2,
                 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 2, 2, 0, 2, 0, 1, 2, 2, 1, 0, 2, 2, 0, 0, 0, 2, 0, 0,
                 0, 1, 2, 1, 0, 2, 2, 1, 2, 0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 0, 2, 0, 0, 2, 1, 2, 2, 2, 1, 0, 0, 1, 1, 1,
                 0, 0, 2, 0, 1, 1, 0, 0, 0, 1, 0, 2, 0, 0, 1, 1, 2, 0, 2, 0, 2, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 2,
                 1, 0, 1, 0, 1, 2, 0, 0, 1, 2, 0, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 1, 2, 2, 1, 1, 0, 2, 2, 2, 2, 1, 2, 0,
                 2, 0, 2, 2, 1, 1, 0, 1, 0, 0, 1, 2, 2, 1, 1, 1, 0, 1, 0, 1, 2, 0, 2, 1, 2, 2, 0, 2, 2, 0, 1, 1, 0, 0,
                 1, 1, 1, 1, 1, 0, 1, 2, 0, 2, 2, 0, 1, 2, 2, 1, 1, 2, 0, 1, 1, 1, 2, 0, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1,
                 0, 1, 2, 0, 1, 1, 1, 0, 2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 2, 2, 2, 1, 1, 1, 2, 2, 0, 2, 1, 0, 2, 2, 2, 2,
                 2, 2, 0, 0, 1, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 1, 1, 2, 0, 2, 2, 0, 2, 1, 0, 0, 1, 1,
                 1, 1, 2, 1, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 2, 1, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 1, 1, 1, 0,
                 2, 2, 1, 0, 2, 1, 0, 2, 0, 1, 0, 0, 2, 1, 0, 1, 0, 2, 2, 2, 1, 2, 2, 0, 2, 1, 0, 2, 0, 2, 1, 1, 2, 0,
                 1, 2, 0, 0, 1, 1, 1, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 1, 0, 1, 2, 1, 1, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1,
                 2, 2, 2, 1, 1, 2, 0, 1, 2, 1, 2, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 0, 2, 0, 0, 0, 2, 1, 0, 1, 2, 0, 1, 1,
                 2, 1, 1, 2, 2, 0, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 2, 1, 1, 0, 1, 2, 2, 1,
                 0, 2, 2, 1, 2, 0, 1, 2, 2, 2, 0, 1, 0, 0, 1, 0, 2, 1, 0, 1, 1, 1, 1, 2, 1, 2, 0, 1, 2, 2, 2, 2, 2, 0,
                 1, 0, 2, 2, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2,
                 1, 2, 1, 1, 1, 2, 0, 1, 1, 2, 0, 0, 1, 2, 0, 2, 0, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 0, 1,
                 2, 2, 1, 1, 0, 2, 1, 2, 1, 1, 1, 0, 2, 1, 0, 0, 2, 2, 2, 1, 0, 1, 2, 1, 2, 1, 1, 0, 0, 0, 2, 1, 0, 1,
                 0, 0, 1, 2, 0, 0, 2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 2, 2, 0, 0, 0, 1, 2, 0, 1, 1, 1, 1,
                 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 0, 2, 1, 0, 2, 0, 1, 1, 0, 1, 2, 1, 1, 0,
                 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 2, 2, 0, 1, 2, 1, 2, 2, 2, 2, 0, 2, 1, 1, 0, 0, 0, 1, 1, 2, 2, 0, 0, 0,
                 1, 2, 0, 1, 2, 0, 1, 2, 1, 1, 2, 1, 2, 2, 0, 1, 2, 2, 1, 2, 0, 1, 1, 0, 0, 0, 0, 1, 2, 2, 2, 0, 1, 0,
                 1, 0, 2, 1, 1, 0, 2, 1, 2, 1, 2, 0, 2, 0, 0, 1, 2, 0, 1, 0, 0, 0, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 0, 0,
                 0, 1, 0, 2, 0, 2, 0, 1, 1, 1, 0, 0, 0, 2, 0, 1, 2, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 2, 1, 1, 2, 2, 1, 1,
                 1, 0, 1, 0, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 2, 1, 0, 0, 1, 1, 1, 0, 2,
                 2, 0, 0, 1, 1, 2, 2, 1, 2, 2, 2, 0, 0, 2, 2, 2, 0, 1, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 1, 2, 1, 2, 0, 0,
                 1, 0, 2, 0, 0, 2, 0, 1, 1, 2, 2, 0, 1, 0, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0, 1, 2, 0, 1, 1, 1, 0, 1, 0, 2,
                 2, 0, 2, 1, 0, 0, 1, 2, 0, 0, 1, 0, 1, 0, 2, 2, 1, 0, 1, 2, 2, 0, 2, 2, 0, 0, 1, 1, 1, 2, 1, 2, 2, 2,
                 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 2, 1, 0, 2, 1, 2, 0, 2, 0, 2, 2, 0, 2, 2, 0, 1, 0, 0, 2, 0, 2, 2,
                 1, 0, 2, 0, 2, 2, 1, 1, 2, 2, 2, 1, 0, 0, 1, 2, 1, 0, 1, 0, 2, 2, 1, 2, 1, 2, 0, 1, 0, 1, 2, 2, 1, 0,
                 2, 0, 2, 1, 0, 1, 2, 0, 0, 2, 2, 1, 1, 0, 0, 1, 2, 0, 2, 2, 1, 2, 1, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 0,
                 1, 0, 1, 1, 1, 0, 1, 2, 1, 0, 2, 2, 0, 1, 1, 2, 0, 2, 2, 0, 2, 1, 1, 2, 2, 2, 1, 1, 0, 1, 0, 2, 2, 2,
                 2, 0, 2, 2, 1, 0, 0, 1, 1, 0, 1, 2, 1, 0, 0, 0, 2, 2, 0, 2, 0, 1, 2, 2, 1, 1, 1, 2, 0, 2, 0, 0, 1, 2,
                 0, 1, 1, 0, 1, 1, 1, 2, 0, 0, 0, 2, 1, 0, 2, 1, 2, 1, 0, 1, 1, 2, 2, 0, 1, 0, 2, 2, 2, 1, 1, 0, 1, 2,
                 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 2, 1, 0, 0, 2, 0, 2, 0, 1, 1, 0, 0, 1, 2, 0, 2, 2, 2, 1, 1, 0, 0, 0,
                 0, 1, 0, 1, 2, 2, 2, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, 1,
                 2, 2, 2, 0, 0, 2, 0, 1, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 1, 1, 1, 1, 0, 2, 0, 2, 0, 0, 1, 2, 2,
                 1, 0, 2, 0, 1, 2, 2, 1, 2, 0, 0, 2, 0, 0, 1, 1, 1, 0, 2, 0, 2, 2, 2, 2, 1, 2, 2, 0, 1, 2, 2, 2, 0, 0,
                 0, 1, 0, 1, 2, 0, 0, 0, 0, 1, 2, 0, 0, 2, 2, 0, 1, 1, 2, 2, 2, 2, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0,
                 2, 2, 0, 0, 1, 1, 0, 2, 2, 1, 1, 0, 2, 0, 2, 1, 0, 1, 2, 1, 1, 2, 1, 0, 0, 1, 2, 1, 1, 2, 2, 0, 1, 2,
                 0, 0, 0, 1, 1, 2, 0, 2, 1, 2, 0, 1, 0, 0, 0, 2, 0, 1, 1, 2, 2, 2, 0, 0, 0, 2, 2, 1, 0, 2, 1, 0, 0, 2,
                 1, 1, 2, 0, 2, 0, 2, 0, 1, 2, 2, 0, 0, 0, 2, 2, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 2, 1, 1, 0, 1, 0, 2, 0,
                 1, 0, 2, 0, 2, 1, 0, 1, 2, 0, 0, 2, 1, 1, 0, 0, 1, 0, 2, 1, 1, 1, 2, 1, 2, 2, 0, 2, 2, 1, 2, 2, 2, 1,
                 0, 1, 1, 1, 2, 1, 1, 1, 1, 0, 0, 1, 1, 0, 2, 2, 0, 1, 1, 1, 1, 2, 1, 1, 0, 0, 2, 2, 0, 2, 1, 1, 1, 1,
                 2, 0, 2, 2, 2, 0, 1, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 2, 1, 1, 2, 2, 0, 1, 1, 0, 0, 1, 0, 2, 0, 2, 2, 0,
                 2, 2, 0, 0, 1, 2, 0, 1, 0, 0, 0, 0, 1, 2, 0, 1, 1, 0, 0, 2, 0, 0, 2, 0, 1, 1, 2, 2, 1, 0, 1, 0, 0, 2,
                 2, 2, 0, 0, 1, 0, 2, 0, 1, 2, 1, 0, 1, 1, 2, 2, 2, 2, 0, 0, 0, 2, 1, 1, 2, 0, 1, 1, 1, 0, 0, 0, 1, 0,
                 2, 0, 2, 0, 2, 0, 0, 1, 0, 0, 2, 0, 2, 2, 2, 2, 2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 0, 2, 2,
                 2, 1, 1, 1, 0, 1, 0, 1, 1, 0, 2, 0, 0, 1, 2, 2, 1, 2, 0, 0, 0, 2, 2, 0, 1, 1, 0, 2, 0, 1, 2, 1, 0, 0,
                 0, 1, 1, 1, 2, 0, 1, 1, 1, 2, 1, 0, 2, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 2, 0, 1,
                 1, 2, 0, 0, 1, 1, 0, 1, 1, 0, 2, 0, 1, 1, 2, 2, 1, 0, 2, 1, 2, 0, 0, 0, 2, 2, 2, 0, 1, 1, 0, 0, 1, 1,
                 1, 1, 0, 0, 2, 0, 2, 2, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 1, 1, 1, 2, 0, 2,
                 1, 1, 0, 0, 1, 2, 1, 2, 2, 2, 2, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 2, 0, 2, 2, 2, 0, 1, 0, 1, 2, 2, 0,
                 0, 2, 0, 0, 1, 0, 0, 1, 2, 1, 0, 1, 2, 2, 1, 2, 2, 1, 1, 0, 2, 1, 0, 1, 1, 2, 1, 2, 1, 0, 2, 0, 1, 1,
                 0, 0, 1, 0, 2, 1, 1, 1, 2, 1, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 0, 0, 2, 2, 1, 1, 2, 1, 1,
                 1, 0, 0, 0, 0, 0, 0, 2, 2, 1, 0, 1, 0, 1, 1, 2, 2, 0, 1, 1, 2, 2, 1, 0, 2, 1, 1, 1, 2, 1, 2, 0, 0, 2,
                 0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 2, 1, 0, 2, 1, 1, 0, 1, 0, 0, 2, 2, 1, 1, 2, 0, 0, 0, 1, 1,
                 1, 1, 1, 0, 2, 2, 2, 2, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 2, 2, 1, 0, 1, 1, 0, 2, 0, 2, 2, 1, 1, 1, 1, 0,
                 0, 2, 2, 1, 2, 0, 0, 2, 1, 0, 2, 1, 2, 1, 2, 1, 0, 2, 2, 2, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 2, 2, 2, 1,
                 0, 2, 0, 2, 2, 2, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 2, 1, 2, 0, 0, 0, 1, 2, 0, 1, 2, 0, 1, 0, 0, 0, 1,
                 0, 1, 2, 2, 1, 2, 0, 1, 0, 2, 1, 0, 1, 2, 1, 1, 1, 2, 1, 0, 0, 2, 1, 1, 1, 0, 2, 1, 2, 2, 2, 2, 2, 1,
                 1, 2, 1, 2, 1, 0, 1, 1, 0, 1, 2, 0, 1, 2, 2, 2, 2, 2, 1, 0, 2, 2, 2, 2, 0, 1, 2, 1, 2, 0, 0, 2, 0, 0,
                 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 1, 1, 2, 0, 1, 1, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2, 2, 1, 0, 1, 0, 2, 0, 0,
                 0, 0, 2, 0, 1, 2, 1, 0, 1, 2, 0, 2, 0, 2, 1, 0, 0, 0, 1, 2, 0, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2,
                 0, 2, 2, 2, 1, 2, 1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 2, 2, 1, 0, 2, 0, 2, 0, 1, 0, 1, 0, 2, 0, 1, 1, 1, 1,
                 0, 2, 0, 1, 2, 1, 2, 0, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 0, 0, 2, 0, 2, 2, 2, 0, 1, 2, 1, 0, 2, 0, 2, 2,
                 2, 0, 1, 1, 0, 2, 2, 2, 2, 0, 1, 2, 1, 2, 2, 1, 2, 0, 1, 2, 0, 0, 0, 2, 2, 1, 1, 0, 0, 2, 1, 1, 1, 0,
                 1, 2, 0, 1, 2, 0, 0, 1, 2, 0, 2, 0, 0, 2, 0, 2, 0, 1, 1, 1, 1, 1, 0, 2, 1, 1, 2, 2, 0, 0, 1, 2, 1, 2,
                 2, 1, 0, 2, 2, 2, 2, 2, 0, 1, 0, 0, 1, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 2, 2, 2, 1, 2, 1, 1, 2, 0, 0, 0,
                 0, 1, 1, 1, 0, 1, 0, 2, 0, 1, 1, 2, 2, 0, 0, 1, 2, 0, 2, 2, 1, 2, 0, 0, 1, 0, 1, 2, 2, 0, 1, 2, 1, 2,
                 1, 2, 1, 2, 0, 1, 1, 1, 1, 1, 2, 0, 2, 2, 1, 2, 2, 1, 1, 0, 0, 1, 0, 2, 0, 1, 1, 1, 1, 2, 2, 0, 0, 1,
                 0, 1, 0, 2, 2, 2, 1, 0, 2, 2, 2, 0, 0, 2, 2, 1, 2, 2, 0, 2, 0, 2, 1, 0, 2, 0, 0, 1, 1, 1, 0, 2, 0, 0,
                 0, 1, 0, 2, 1, 2, 1, 2, 1, 0, 1, 2, 0, 2, 0, 1, 2, 2, 1, 0, 1, 2, 1, 2, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0,
                 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 0, 2, 0, 1, 2, 2, 0, 1, 2, 2, 2, 2, 0, 2, 1, 1, 2, 2, 2, 2, 1, 0, 1,
                 0, 2, 2, 0, 1, 0, 2, 2, 0, 0, 0, 0, 2, 0, 2, 1, 0, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 0, 1, 1, 2, 0, 0, 0,
                 0, 2, 0, 0, 1, 2, 1, 2, 2, 2, 1, 0, 1, 1, 1, 1, 0, 0, 2, 0, 2, 1, 0, 2, 2, 1, 0, 0, 2, 1, 2, 2, 2, 1,
                 0, 2, 1, 0, 1, 2, 2, 0, 1, 2, 2, 0, 0, 2, 1, 2, 0, 1, 0, 1, 2, 1, 1, 0, 1, 1, 0, 0, 1, 2, 0, 1, 2, 2,
                 0, 1, 0, 0, 2, 2, 2, 2, 2, 0, 2, 0, 1, 1, 2, 2, 0, 0, 2, 0, 0, 2, 0, 1, 1, 0, 1, 0, 1, 2, 1, 1, 2, 0,
                 0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 0, 1, 2, 2, 0, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 1, 1,
                 0, 0, 2, 2, 1, 2, 0, 2, 2, 0, 0, 1, 1, 0, 2, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 2, 2,
                 1, 0, 2, 2, 0, 1, 0, 0, 1, 2, 0, 0, 0, 1, 0, 2, 0, 2, 0, 0, 2, 2, 1, 1, 0, 0, 2, 0, 0, 2, 1, 0, 2, 1,
                 0, 1, 2, 2, 1, 0, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1, 1, 0, 1, 2, 0, 0, 0, 2, 0, 1, 1, 1, 1, 0, 0, 1, 2,
                 1, 1, 2, 2, 1, 0, 1, 1, 1, 1, 0, 2, 0, 1, 2, 2, 0, 2, 0, 2, 1, 1, 0, 1, 0, 2, 2, 2, 2, 1, 1, 2, 1, 1,
                 2, 0, 0, 2, 0, 0, 1, 0, 0, 2, 2, 0, 2, 1, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1, 1, 1, 1, 1, 0, 1, 2, 0, 0, 2,
                 0, 0, 2, 2, 1, 1, 1, 0, 0, 0, 2, 0, 2, 0, 1, 2, 2, 0, 2, 2, 2, 0, 1, 0, 1, 2, 2, 2, 1, 0, 2, 1, 1, 2,
                 0, 1, 2, 2, 1, 0, 2, 2, 1, 2, 0, 1, 2, 1, 0, 2, 0, 0, 2, 2, 1, 1, 0, 2, 0, 0, 2, 2, 0, 1, 0, 1, 2, 0,
                 1, 0, 1, 2, 0, 0, 1, 1, 1, 0, 1, 1, 0, 2, 2, 2, 0, 1, 0, 1, 1, 0, 2, 1, 0, 1, 0, 0, 2, 0, 0, 1, 2, 0,
                 2, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0, 2, 0, 0, 1, 1, 0, 0, 2, 0, 0, 2, 1, 2, 1, 2, 2, 1, 2, 1,
                 0, 1, 2, 0, 2, 0, 1, 2, 2, 0, 2, 2, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 2, 1, 0, 1, 0, 1, 0, 2, 2, 2,
                 2, 2, 1, 2, 0, 1, 2, 2, 1, 0, 1, 2, 0, 1, 1, 0, 1, 2, 0, 1, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 1, 2, 2, 0,
                 0, 1, 2, 2, 1, 1, 1, 2, 0, 2, 0, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 0, 0, 1, 2, 1, 2, 0, 0, 2,
                 0, 0, 2, 1, 1, 1, 2, 0, 1, 2, 0, 1, 1, 0, 1, 1, 2, 0, 2, 2, 0, 1, 2, 2, 2, 0, 1, 2, 0, 2, 2, 0, 0, 1,
                 0, 0, 0, 0, 2, 0, 1, 0, 0, 2, 0, 0, 0, 2, 1, 0, 2, 0, 1, 1, 1, 0, 2, 0, 0, 1, 0, 2, 2, 1, 0, 0, 1, 1,
                 0, 1, 2, 1, 1, 2, 2, 2, 0, 1, 0, 2, 2, 2, 1, 1, 2, 2, 0, 1, 2, 0, 0, 1, 1, 2, 0, 1, 2, 1, 2, 1, 2, 2,
                 1, 2, 2, 0, 1, 1, 2, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 2, 1, 2, 2, 2, 0, 0, 1, 2, 0, 0, 2, 1, 1, 2, 0,
                 0, 2, 1, 1, 0, 0, 1, 2, 2, 0, 1, 2, 0, 1, 0, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 2, 0, 1, 0, 2, 2, 1, 2, 1,
                 1, 1, 0, 2, 2, 1, 1, 2, 2, 0, 2, 1, 2, 2, 2, 1, 1, 2, 1, 0, 0, 1, 1, 0, 2, 1, 0, 2, 2, 2, 2, 0, 0, 0,
                 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 2, 1, 0, 2, 1, 0, 0, 2, 0, 2, 2, 1, 2, 0, 2, 1, 2, 2, 1, 2, 0, 0,
                 2, 2, 0, 0, 1, 0, 1, 2, 1, 1, 0, 2, 1, 0, 1, 2, 2, 2, 1, 1, 2, 0, 1, 1, 2, 1, 2, 0, 2, 1, 0, 2, 1, 2,
                 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 1, 2, 0, 0, 2, 1, 2, 0, 2, 1, 2, 0, 1, 1, 2, 0, 0, 1, 1, 0, 0, 2,
                 0, 1, 2, 1, 1, 0, 1, 0, 2, 2, 2, 2, 1, 2, 0, 2, 1, 2, 2, 1, 1, 1, 0, 1, 2, 2, 1, 2, 0, 0, 0, 2, 1, 1,
                 1, 0, 2, 0, 1, 0, 2, 0, 0, 2, 0, 2, 1, 1, 1, 2, 0, 1, 0, 0, 2, 2, 1, 0, 0, 0, 2, 2, 0, 2, 1, 1, 0, 1,
                 1, 2, 1, 2, 2, 0, 0, 1, 2, 2, 2, 2, 2, 1, 2, 0, 1, 2, 1, 0, 2, 2, 2, 2, 2, 1, 2, 1, 2, 0, 0, 1, 1, 2,
                 2, 1, 0, 1, 2, 0, 2, 0, 1, 2, 2, 1, 2, 1, 0, 0, 1, 2, 0, 1, 1, 0, 2, 2, 2, 0, 1, 2, 2, 1, 0, 1, 2, 1,
                 0, 2, 2, 2, 2, 0, 1, 0, 2, 0, 0, 0, 1, 1, 2, 2, 2, 0, 2, 2, 2, 0, 2, 1, 0, 2, 1, 2, 1, 2, 2, 1, 0, 1,
                 1, 2, 2, 0, 1, 2, 1, 2, 1, 2, 2, 0, 2, 0, 1, 1, 0, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1, 1, 2, 1, 2, 1, 1, 2,
                 1, 1, 0, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 0, 1, 2, 1, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0,
                 0, 1, 2, 2, 2, 2, 1, 0, 2, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 2, 2, 0, 2, 1, 2, 1, 2, 2, 1, 0, 1, 0, 2, 2,
                 0, 2, 2, 1, 1, 0, 0, 1, 1, 0, 2, 2, 2, 0, 1, 0, 1, 0, 0, 1, 0, 2, 1, 2, 2, 0, 0, 2, 0, 0, 2, 0, 2, 1,
                 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 2, 2, 1, 1, 2, 1, 2, 0, 2, 1, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 0, 1, 2,
                 0, 2, 2, 2, 0, 1, 0, 0, 2, 2, 1, 1, 2, 1, 2, 2, 0, 2, 2, 2, 2, 0, 0, 0, 1, 0, 2, 0, 0, 2, 1, 2, 0, 2,
                 2, 2, 2, 2, 2, 1, 2, 0, 2, 2, 2, 2, 1, 1, 0, 0, 1, 2, 0, 2, 0, 2, 0, 2, 2, 0, 1, 2, 1, 2, 0, 2, 2, 1,
                 2, 1, 0, 0, 1, 2, 1, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 0, 2, 2, 0, 0, 0, 2, 1, 2, 2, 0, 1, 0, 0, 2, 1,
                 1, 1, 0, 1, 1, 2, 2, 1, 1, 0, 0, 1, 1, 0, 2, 0, 2, 1, 0, 0, 1, 2, 2, 1, 0, 2, 2, 1, 1, 0, 1, 0, 0, 0,
                 0, 1, 1, 1, 1, 1, 0, 2, 1, 0, 2, 2, 0, 2, 1, 1, 0, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 0, 2, 2,
                 2, 1, 1, 1, 0, 2, 1, 2, 1, 0, 1, 1, 0, 0, 0, 2, 1, 2, 2, 1, 1, 2, 0, 1, 0, 2, 0, 0, 2, 2, 1, 0, 2, 1,
                 2, 0, 2, 2, 2, 2, 0, 0, 0, 1, 0, 2, 1, 1, 0, 2, 1, 2, 2, 1, 2, 2, 1, 0, 1, 2, 2, 0, 1, 0, 1, 2, 2, 1,
                 1, 1, 0, 0, 0, 1, 2, 2, 1, 2, 2, 0, 2, 2, 1, 0, 0, 2, 0, 1, 1, 2, 1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 1,
                 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 2, 0, 2, 1, 2, 0, 1, 1, 1, 0, 0, 2, 2, 1,
                 1, 0, 1, 0, 0, 1, 0, 1, 0, 2, 0, 2, 0, 1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 0, 0, 2, 0, 1, 1, 2, 2, 2, 1, 1,
                 0, 1, 2, 2, 2, 0, 2, 2, 0, 1, 1, 1, 1, 1, 2, 0, 0, 2, 2, 2, 0, 0, 0, 1, 1, 2, 0, 2, 1, 0, 1, 1, 2, 1,
                 1, 2, 2, 2, 2, 2, 2, 0, 0, 2, 1, 2, 2, 2, 1, 2, 0, 0, 2, 1, 1, 0, 1, 0, 2, 0, 1, 2, 2, 0, 0, 0, 2, 0,
                 1, 0, 1, 2, 1, 0, 1, 2, 2, 1, 0, 0, 1, 1, 0, 2, 2, 0, 1, 2, 1, 1, 0, 1, 1, 2, 1, 2, 2, 1, 0, 2, 0, 2,
                 1, 0, 0, 2, 2, 1, 1, 0, 0, 1, 1, 0, 0, 2, 0, 0, 2, 0, 2, 0, 2, 1, 1, 2, 1, 0, 0, 0, 0, 2, 0, 0, 1, 1,
                 2, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 1, 2, 1, 2, 1, 2, 0, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 0, 2, 1, 0, 1, 2,
                 1, 1, 0, 2, 1, 2, 0, 1, 1, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 2, 2, 0, 2, 1, 0, 0, 1,
                 1, 2, 2, 2, 0, 1, 1, 0, 1, 0, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 2, 2, 0, 1, 1, 1, 1, 0, 0, 2, 1, 2,
                 0, 0, 0, 1, 1, 2, 2, 0, 0, 0, 1, 2, 1, 0, 1, 1, 2, 1, 1, 0, 0, 2, 2, 2, 0, 1, 0, 0, 2, 1, 0, 1, 0, 0,
                 0, 2, 1, 2, 1, 0, 2, 0, 0, 1, 2, 2, 1, 2, 1, 2, 0, 0, 1, 1, 0, 1, 1, 1, 1, 2, 2, 1, 2, 0, 2, 1, 0, 0,
                 0, 2, 2, 2, 0, 1, 2, 1, 1, 0, 1, 2, 1, 0, 0, 0, 2, 0, 0, 1, 2, 2, 0, 0, 1, 0, 0, 1, 0, 2, 1, 0, 2, 2,
                 2, 0, 2, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 1, 1, 0, 1, 0, 0, 1, 0, 0,
                 0, 2, 1, 2, 2, 2, 1, 0, 1, 0, 2, 2, 0, 0, 0, 1, 2, 0, 2, 2, 1, 1, 1, 0, 2, 2, 0, 2, 2, 0, 1, 2, 2, 0,
                 1, 1, 1, 1, 2, 2, 0, 2, 2, 2, 2, 1, 1, 0, 2, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 2, 1, 2, 0, 1, 0, 2, 1,
                 2, 2, 2, 2, 0, 2, 1, 0, 2, 0, 2, 0, 2, 2, 0, 0, 2, 0, 2, 1, 2, 2, 0, 0, 1, 2, 0, 1, 1, 2, 0, 0, 2, 0,
                 1, 0, 0, 2, 0, 1, 2, 2, 1, 0, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 2, 0, 2, 2, 2, 2, 1, 0, 2, 2,
                 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 2, 1, 1, 2, 1, 1, 0, 1, 0, 1, 1, 2, 0, 2, 1, 0, 0, 0, 2, 0, 2, 0, 0, 2,
                 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 2, 0, 1, 2, 1, 0, 1, 0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 1, 1, 0,
                 1, 1, 0, 2, 0, 2, 2, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2, 2, 0, 1, 0, 1, 2, 0, 1,
                 1, 2, 0, 0, 2, 0, 2, 0, 0, 1, 2, 2, 2, 0, 0, 2, 0, 1, 1, 2, 2, 0, 0, 2, 1, 1, 0, 1, 1, 0, 2, 0, 0, 2,
                 2, 0, 0, 2, 0, 1, 2, 1, 2, 0, 2, 1, 1, 1, 0, 2, 0, 0, 2, 2, 2, 2, 2, 1, 2, 0, 2, 1, 1, 2, 2, 2, 0, 0,
                 1, 0, 0, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 0, 1, 0, 0, 1, 1, 0, 1, 1, 2, 0, 2, 1, 1, 0, 1, 1, 1, 0, 0,
                 1, 1, 1, 0, 1, 1, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 1, 2, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 2, 1, 2, 1, 0,
                 1, 2, 2, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 1, 1, 2, 1, 2, 1, 0, 1, 1, 1, 1, 2, 1, 1, 2, 0, 1, 2, 1, 0, 2,
                 2, 2, 0, 0, 2, 2, 0, 0, 2, 1, 0, 0, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 0, 1, 1, 0, 2, 1, 2, 1, 2, 1, 2, 1,
                 2, 2, 1, 2, 0, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 0, 2, 2, 1, 2, 1, 2,
                 2, 2, 0, 0, 0, 1, 1, 0, 2, 1, 0, 1, 1, 2, 1, 0, 2, 1, 0, 1, 0, 0, 2, 2, 1, 2, 1, 0, 1, 1, 0, 1, 1, 2,
                 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 1, 1, 2, 2, 1, 0, 0, 2, 1, 0, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 0, 1, 1, 1,
                 2, 0, 2, 0, 0, 1, 2, 0, 2, 2, 0, 2, 2, 0, 0, 2, 1, 2, 1, 1, 0, 2, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 0, 1,
                 1, 2, 1, 1, 1, 2, 2, 1, 0, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 2, 0, 2, 0, 1, 2, 2, 0, 1, 1, 2, 1, 2, 0, 2,
                 1, 0, 1, 0, 1, 2, 1, 2, 0, 2, 1, 2, 1, 0, 1, 1, 1, 0, 1, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2, 2, 0, 0,
                 2, 2, 0, 2, 1, 2, 0, 1, 0, 2, 1, 1, 2, 1, 2, 0, 2, 1, 2, 1, 1, 2, 2, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0,
                 2, 0, 0, 0, 0, 0, 2, 1, 2, 0, 1, 1, 2, 0, 2, 2, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 1, 2, 0, 1, 2, 0, 0, 2,
                 0, 0, 2, 0, 1, 2, 2, 2, 2, 2, 0, 1, 0, 2, 2, 1, 1, 2, 2, 2, 1, 0, 2, 2, 2, 2, 1, 0, 0, 2, 2, 1, 1, 1,
                 1, 1, 1, 2, 2, 0, 2, 2, 1, 1, 2, 0, 1, 0, 1, 2, 2, 0, 2, 2, 2, 0, 2, 1, 1, 1, 2, 0, 0, 0, 1, 2, 0, 1,
                 0, 1, 0, 1, 1, 2, 2, 1, 0, 0, 2, 0, 1, 2, 0, 0, 1, 2, 1, 1, 2, 2, 1, 0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 1,
                 0, 2, 0, 2, 1, 1, 1, 0, 2, 2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 2, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0,
                 2, 1, 0, 2, 1, 1, 1, 2, 0, 1, 1, 2, 1, 0, 1, 2, 0, 2, 1, 2, 0, 0, 1, 1, 0, 1, 1, 2, 0, 2, 2, 0, 2, 1,
                 0, 0, 2, 2, 0, 2, 1, 2, 1, 1, 1, 1, 2, 2, 0, 1, 2, 2, 0, 2, 1, 1, 1, 2, 0, 0, 1, 0, 0, 0, 2, 1, 1, 0,
                 0, 0, 1, 0, 0, 2, 2, 0, 1, 1, 0, 2, 1, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 0,
                 0, 0, 1, 0, 1, 2, 2, 2, 1, 1, 1, 1, 0, 2, 2, 1, 1, 1, 0, 2, 0, 2, 0, 2, 1, 2, 2, 1, 2, 1, 0, 1, 1, 2,
                 1, 2, 2, 1, 0, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 2, 1, 2, 0, 2, 0, 1, 0, 2, 1, 0, 0, 2, 0, 1, 2, 0, 2,
                 2, 1, 1, 1, 0, 0, 2, 0, 1, 1, 1, 1, 2, 0, 1, 1, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 2, 1,
                 2, 1, 1, 2, 2, 2, 1, 1, 0, 2, 2, 0, 2, 2, 2, 0, 2, 0, 1, 1, 0, 1, 2, 1, 2, 1, 1, 2, 0, 0, 1, 2, 1, 1,
                 0, 1, 2, 1, 2, 2, 1, 2, 1, 1, 0, 2, 2, 1, 0, 2, 0, 1, 2, 1, 1, 2, 0, 1, 2, 2, 1, 2, 0, 1, 2, 1, 1, 2,
                 0, 2, 1, 1, 0, 2, 2, 2, 0, 2, 0, 1, 1, 0, 0, 1, 0, 1, 2, 2, 1, 1, 0, 1, 1, 1, 1, 1, 2, 2, 0, 2, 1, 1,
                 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 2, 2, 1, 2, 0, 1, 2, 1, 0, 0, 0, 1, 0, 0, 1, 2, 1, 1, 0, 2, 0, 0,
                 0, 0, 0, 1, 0, 1, 2, 1, 2, 2, 2, 0, 2, 1, 1, 2, 2, 1, 0, 1, 0, 0, 1, 1, 2, 1, 2, 0, 1, 2, 2, 2, 0, 2,
                 2, 0, 0, 2, 1, 2, 1, 2, 1, 0, 2, 2, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 2, 0, 1, 1, 2, 1,
                 0, 1, 2, 0, 2, 2, 2, 1, 2, 2, 1, 1, 2, 0, 2, 1, 1, 0, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 0, 0,
                 2, 0, 0, 1, 0, 2, 0, 2, 0, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 1, 0, 2, 2, 1, 2, 1, 1, 0, 2, 2, 2, 2, 0, 2,
                 1, 0, 2, 1, 2, 2, 0, 1, 1, 1, 0, 1, 2, 1, 2, 0, 1, 2, 2, 0, 2, 2, 2, 0, 1, 1, 0, 2, 1, 0, 0, 2, 1, 0,
                 1, 0, 0, 1, 1, 1, 1, 2, 0, 1, 0, 1, 1, 2, 2, 2, 0, 0, 2, 1, 1, 1, 2, 2, 0, 0, 0, 0, 2, 0, 1, 1, 1, 2,
                 0, 0, 1, 1, 1, 2, 0, 0, 1, 0, 2, 0, 0, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 0, 1, 1, 1,
                 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 0, 1, 1, 2, 2, 0, 1, 2, 2, 1, 2, 1, 0, 1,
                 2, 1, 0, 2, 1, 1, 1, 2, 2, 1, 1, 0, 0, 0, 1, 1, 2, 1, 0, 2, 1, 0, 1, 2, 1, 1, 1, 1, 2, 2, 0, 2, 1, 1,
                 1, 1, 2, 0, 0, 1, 1, 2, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 1, 2, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2,
                 0, 0, 1, 0, 0, 2, 0, 1, 0, 2, 0, 1, 2, 1, 1, 1, 1, 2, 0, 2, 0, 2, 0, 0, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1,
                 2, 0, 0, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 0, 0, 0, 2,
                 0, 2, 2, 0, 1, 0, 1, 2, 1, 1, 0, 0, 1, 1, 2, 2, 0, 1, 1, 2, 2, 1, 2, 0, 1, 2, 1, 0, 2, 2, 1, 0, 1, 0,
                 1, 1, 0, 2, 2, 2, 1, 2, 0, 2, 2, 2, 2, 2, 1, 0, 1, 1, 2, 1, 2, 1, 2, 0, 0, 0, 0, 2, 0, 2, 2, 1, 1, 1,
                 1, 2, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 0, 1, 2, 1, 0, 1, 0, 2, 0, 2, 0, 0, 2, 2, 0, 0, 1, 2, 1, 0, 1,
                 0, 2, 1, 0, 2, 2, 2, 2, 2, 2, 0, 0, 1, 2, 2, 2, 2, 0, 1, 0, 2, 1, 2, 2, 2, 0, 2, 2, 2, 1, 1, 2, 2, 1,
                 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 2, 0, 2, 2, 1, 2, 2, 2, 0, 0, 2, 1, 1, 2, 1, 2, 2,
                 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 1, 0, 0, 1, 0, 2, 2, 1, 0, 2, 2, 0, 1, 0, 2, 1, 0, 0,
                 2, 0, 0, 2, 1, 2, 2, 2, 0, 0, 1, 0, 0, 2, 0, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 0, 1, 0, 2, 1,
                 2, 0, 2, 1, 0, 2, 0, 1, 1, 0, 1, 1, 2, 2, 0, 0, 2, 1, 0, 2, 0, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 0,
                 2, 1, 2, 2, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 1, 1, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 2, 1, 0, 0, 2, 2, 1, 2,
                 2, 2, 0, 1, 2, 1, 1, 1, 2, 2, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 2,
                 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 1, 2, 2, 1, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 2, 0,
                 2, 1, 1, 1, 0, 0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2, 0, 0, 0, 0, 2, 1, 1, 1, 0, 1, 2, 2, 1, 0, 0, 0, 1,
                 1, 0, 0, 1, 0, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 2, 2, 2, 1, 2, 1, 2, 1, 0, 2, 1, 0, 1, 1, 1, 1,
                 0, 0, 2, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 2, 0, 0, 2, 0, 1, 1, 0, 1, 1, 1, 2, 1, 0, 0, 1, 2, 0, 1, 1,
                 0, 2, 1, 1, 2, 1, 0, 1, 2, 0, 1, 1, 0, 1, 1, 0, 2, 2, 1, 0, 1, 1, 0, 0, 0, 2, 2, 2, 1, 0, 2, 0, 1, 0,
                 2, 2, 1, 2, 0, 0, 1, 2, 1, 0, 1, 0, 1, 2, 2, 2, 2, 1, 2, 1, 0, 2, 1, 2, 2, 2, 2, 2, 0, 2, 2, 0, 1, 1,
                 2, 2, 2, 0, 2, 2, 2, 0, 0, 2, 1, 1, 1, 0, 0, 1, 0, 0, 2, 1, 1, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 1, 1, 2,
                 0, 1, 1, 0, 1, 2, 0, 1, 2, 0, 2, 2, 2, 1, 0, 2, 2, 2, 1, 0, 0, 2, 2, 2, 0, 2, 0, 2, 1, 1, 0, 1, 0, 0,
                 1, 2, 1, 1, 2, 1, 1, 0, 2, 0, 0, 1, 1, 0, 2, 1, 2, 1, 1, 1, 2, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0,
                 1, 0, 0, 2, 2, 1, 2, 0, 0, 2, 1, 2, 1, 2, 2, 0, 1, 1, 0, 1, 1, 2, 0, 0, 1, 2, 0, 0, 0, 2, 0, 2, 2, 0,
                 0, 2, 1, 2, 2, 2, 0, 0, 1, 1, 2, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 2, 2, 1, 0, 1, 1,
                 1, 1, 2, 0, 0, 1, 0, 2, 1, 0, 2, 1, 1, 0, 1, 1, 0, 1, 2, 2, 0, 0, 1, 1, 2, 0, 2, 1, 0, 2, 2, 0, 2, 1,
                 0, 0, 1, 0, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 0, 1, 2, 0, 1, 1, 1, 2, 0, 0, 0, 0, 2, 2, 2, 0, 1, 0, 1, 1,
                 0, 0, 2, 2, 0, 2, 0, 1, 2, 1, 1, 1, 0, 1, 0, 2, 0, 1, 2, 0, 2, 2, 0, 1, 1, 1, 2, 1, 1, 0, 1, 2, 2, 0,
                 1, 0, 1, 0, 1, 2, 1, 1, 0, 0, 2, 1, 2, 2, 2, 0, 1, 2, 0, 2, 1, 1, 0, 2, 1, 2, 1, 2, 0, 2, 0, 0, 1, 0,
                 1, 0, 1, 1, 0, 1, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 1, 0, 0, 0, 1, 0, 2, 2, 1, 0, 1, 1,
                 0, 2, 2, 1, 0, 2, 2, 1, 1, 0, 0, 0, 1, 2, 2, 1, 2, 0, 2, 0, 1, 0, 2, 2, 0, 0, 2, 0, 1, 2, 2, 1, 1, 2,
                 2, 1, 1, 1, 2, 0, 0, 0, 0, 2, 0, 0, 1, 1, 2, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 2, 0, 0, 1, 1, 2, 2, 2, 0,
                 0, 1, 0, 0, 2, 1, 2, 1, 2, 0, 1, 2, 2, 0, 2, 1, 1, 0, 0, 0, 2, 0, 2, 0, 1, 2, 0, 1, 2, 1, 0, 1, 1, 0,
                 0, 0, 1, 2, 1, 0, 2, 0, 2, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 2, 1, 0, 2, 1, 1, 0, 1, 1, 2, 1, 1, 1, 0,
                 2, 2, 2, 1, 0, 1, 0, 1, 2, 1, 2, 1, 2, 0, 0, 2, 2, 1, 0, 2, 2, 2, 2, 2, 0, 1, 0, 1, 1, 2, 1, 1, 2, 1,
                 1, 1, 2, 1, 1, 2, 1, 0, 0, 2, 2, 0, 0, 1, 1, 2, 1, 1, 0, 0, 0, 2, 0, 2, 2, 1, 0, 2, 0, 0, 1, 2, 1, 2,
                 2, 1, 2, 0, 0, 2, 0, 0, 0, 2, 2, 1, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 2, 0, 0, 0, 0, 1, 0,
                 0, 1, 2, 1, 2, 2, 2, 0, 2, 2, 0, 1, 2, 0, 1, 0, 2, 0, 2, 1, 1, 1, 0, 2, 1, 2, 1, 2, 0, 1, 0, 2, 2, 2,
                 0, 1, 1, 1, 2, 2, 2, 0, 1, 0, 2, 2, 2, 2, 0, 0, 0, 2, 1, 2, 2, 1, 2, 0, 1, 1, 1, 0, 0, 1, 1, 1, 2, 1,
                 1, 2, 2, 2, 0, 0, 0, 2, 2, 1, 1, 0, 2, 1, 2, 1, 1, 2, 1, 1, 2, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 0,
                 0, 2, 1, 2, 0, 2, 2, 1, 1, 1, 2, 2, 0, 1, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 1, 2, 0, 2, 1, 0, 1, 2, 2, 2,
                 0, 2, 2, 2, 2, 1, 2, 1, 2, 2, 0, 0, 2, 2, 0, 1, 2, 0, 2, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 0, 1,
                 1, 0, 0, 1, 0, 2, 2, 0, 1, 2, 1, 0, 2, 2, 0, 1, 0, 2, 2, 1, 1, 0, 2, 1, 1, 2, 2, 1, 2, 2, 1, 0, 1, 2,
                 0, 1, 1, 1, 0, 2, 0, 0, 2, 2, 0, 2, 1, 0, 2, 0, 1, 0, 0, 1, 0, 1, 0, 2, 2, 1, 1, 0, 1, 0, 1, 0, 1, 2,
                 2, 2, 2, 1, 2, 1, 0, 0, 2, 1, 0, 0, 0, 1, 2, 2, 0, 1, 1, 2, 2, 0, 1, 0, 0, 1, 0, 1, 1, 1, 2, 0, 2, 0,
                 0, 1, 1, 1, 0, 1, 1, 2, 2, 2, 1, 0, 0, 2, 2, 0, 2, 2, 1, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 1, 0, 2, 1,
                 0, 1, 1, 0, 2, 0, 0, 0, 0, 2, 1, 1, 2, 0, 0, 2, 1, 0, 0, 1, 2, 1, 1, 0, 0, 0, 2, 2, 2, 1, 2, 1, 0, 1,
                 1, 1, 0, 1, 0, 0, 2, 0, 0, 1, 0, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 1, 1, 0, 2, 1, 1, 1, 2, 1, 0, 0, 1, 0,
                 2, 2, 2, 0, 1, 1, 0, 1, 1, 2, 0, 1, 2, 1, 0, 2, 1, 0, 0, 2, 1, 0, 2, 1, 2, 2, 1, 2, 0, 2, 2, 0, 0, 1,
                 0, 2, 2, 1, 2, 1, 2, 2, 1, 1, 0, 0, 2, 2, 1, 1, 2, 2, 1, 2, 0, 0, 0, 2, 2, 2, 0, 1, 0, 2, 1, 2, 2, 2,
                 2, 2, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 2, 1, 2, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 2, 0, 0, 1, 1, 2, 0, 2,
                 1, 0, 0, 2, 0, 1, 2, 0, 0, 0, 1, 1, 0, 2, 0, 2, 0, 2, 0, 0, 1, 1, 0, 0, 0, 2, 0, 2, 1, 0, 1, 0, 1, 0,
                 1, 2, 1, 1, 0, 0, 1, 2, 1, 0, 2, 0, 1, 1, 1, 2, 2, 2, 2, 0, 1, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 2, 2,
                 1, 1, 1, 2, 0, 1, 0, 0, 1, 1, 1, 1, 1, 2, 0, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 0, 2, 2, 2, 1, 1, 2, 1, 1,
                 0, 1, 2, 0, 1, 2, 0, 2, 0, 2, 2, 0, 2, 1, 0, 2, 0, 1, 1, 0, 2, 1, 1, 2, 0, 1, 1, 1, 2, 1, 2, 1, 2, 2,
                 1, 1, 0, 0, 2, 2, 1, 2, 0, 1, 1, 2, 1, 1, 1, 1, 0, 1, 0, 2, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2,
                 1, 2, 2, 1, 1, 2, 1, 0, 1, 2, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 2, 0, 2, 1, 1, 0, 2,
                 2, 2, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 2, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1,
                 2, 0, 1, 0, 2, 1, 1, 1, 0, 2, 1, 2, 0, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 1, 0, 1, 0, 0, 0, 1, 1,
                 0, 2, 1, 2, 1, 2, 2, 0, 1, 2, 0, 2, 1, 1, 0, 1, 1, 1, 2, 0, 0, 1, 2, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2, 1,
                 0, 1, 2, 1, 0, 1, 1, 1, 0, 1, 1, 2, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 2, 2, 0, 2, 2, 0, 1, 1, 2, 1, 2, 0,
                 2, 1, 0, 2, 1, 1, 1, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 1, 0, 2, 2, 0, 1, 1, 0, 2, 2, 1, 1, 0, 2, 1, 2, 0,
                 0, 2, 1, 1, 2, 0, 0, 0, 0, 2, 2, 0, 1, 1, 0, 2, 2, 1, 2, 1, 1, 0, 2, 2, 0, 1, 2, 1, 2, 1, 0, 1, 1, 0,
                 0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2, 1, 2, 2, 1, 0, 2, 2,
                 1, 2, 2, 0, 2, 0, 1, 0, 0, 1, 2, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 1, 0, 2, 2, 2, 0, 2, 1,
                 2, 1, 2, 0, 1, 1, 0, 0, 0, 2, 2, 1, 1, 1, 2, 0, 2, 1, 1, 1, 0, 0, 1, 2, 2, 0, 0, 0, 1, 1, 2, 1, 2, 0,
                 2, 1, 2, 2], 25000000)
        )