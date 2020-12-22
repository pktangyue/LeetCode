import unittest


class TestSolution(unittest.TestCase):

    def test_MinTimeToVisitAllPoints(self):
        Solution = __import__('1266_MinimumTimeVisitingAllPoints').Solution
        self.assertEqual(
            7,
            Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]),
        )
        self.assertEqual(
            5,
            Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]),
        )
