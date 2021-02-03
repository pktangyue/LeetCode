import unittest


class TestSolution(unittest.TestCase):

    def test_minCostConnectPoints(self):
        Solution = __import__('1584_MinCostToConnectAllPoints').Solution
        self.assertEqual(
            20,
            Solution().minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
        )
        self.assertEqual(
            20,
            Solution().minCostConnectPoints(points=[[0, 0], [2, 2], [4, 10], [5, 2], [7, 0]])
        )
        self.assertEqual(
            18,
            Solution().minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]])
        )
        self.assertEqual(
            4000000,
            Solution().minCostConnectPoints(points=[[-1000000, -1000000], [1000000, 1000000]])
        )
        self.assertEqual(
            0,
            Solution().minCostConnectPoints(points=[[0, 0]])
        )
