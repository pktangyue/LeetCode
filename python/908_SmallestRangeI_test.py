import unittest


class TestSolution(unittest.TestCase):

    def test_SmallestRangeI(self):
        Solution = __import__('908_SmallestRangeI').Solution
        self.assertEqual(
            0,
            Solution().smallestRangeI([1], 0)
        )
        self.assertEqual(
            6,
            Solution().smallestRangeI([0, 10], 2)
        )
        self.assertEqual(
            0,
            Solution().smallestRangeI([1, 3, 6], 3)
        )
