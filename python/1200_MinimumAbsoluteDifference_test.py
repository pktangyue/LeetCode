import unittest


class TestSolution(unittest.TestCase):

    def test_MinimumAbsDifference(self):
        Solution = __import__('1200_MinimumAbsoluteDifference').Solution
        self.assertEqual(
            [[1, 2], [2, 3], [3, 4]],
            Solution().minimumAbsDifference([4, 2, 1, 3])
        )
        self.assertEqual(
            [[1, 3]],
            Solution().minimumAbsDifference([1, 3, 6, 10, 15])
        )
        self.assertEqual(
            [[-14, -10], [19, 23], [23, 27]],
            Solution().minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27])
        )
