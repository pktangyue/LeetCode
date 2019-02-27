import unittest


class TestSolution(unittest.TestCase):

    def test_FindMinArrowShots(self):
        Solution = __import__('452_MinimumNumberOfArrowsToBurstBalloons').Solution
        self.assertEqual(
            2,
            Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
        )
        self.assertEqual(
            2,
            Solution().findMinArrowShots([[1, 3], [1, 7], [4, 10], [8, 10]])
        )
