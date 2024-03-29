import unittest


class TestSolution(unittest.TestCase):

    def test_minCost(self):
        Solution = __import__('1368_MinimumCostToMakeAtLeastOneValidPathInAGrid').Solution
        self.assertEqual(
            44,
            Solution().minCost(grid=[[2, 3, 2, 4, 4, 1, 3, 2, 1, 4, 2, 3, 1, 2, 2, 1], [3, 1, 1, 2, 1, 2, 1, 1, 3, 2, 1, 1, 2, 2, 4, 4], [3, 1, 2, 4, 4, 2, 4, 3, 4, 4, 4, 4, 4, 4, 2, 4],
                                     [4, 1, 4, 1, 1, 2, 2, 4, 1, 2, 4, 4, 2, 2, 2, 3], [1, 2, 1, 2, 2, 3, 3, 1, 3, 3, 2, 1, 3, 1, 1, 1], [3, 2, 2, 4, 3, 1, 1, 3, 4, 3, 1, 2, 4, 3, 2, 3],
                                     [1, 2, 2, 1, 4, 3, 4, 4, 1, 4, 1, 1, 3, 4, 3, 1], [3, 2, 4, 2, 1, 1, 1, 3, 3, 4, 2, 4, 3, 4, 2, 2], [1, 1, 4, 3, 2, 1, 4, 2, 3, 2, 3, 2, 1, 4, 2, 2],
                                     [1, 1, 1, 1, 1, 2, 4, 2, 2, 3, 2, 4, 2, 1, 2, 2], [4, 2, 1, 2, 2, 3, 2, 4, 2, 1, 4, 4, 1, 1, 2, 1], [2, 4, 3, 1, 1, 3, 3, 3, 2, 3, 1, 1, 2, 2, 4, 3],
                                     [2, 3, 2, 3, 1, 3, 4, 3, 1, 3, 1, 3, 3, 1, 2, 4], [3, 2, 2, 4, 1, 1, 4, 3, 1, 1, 1, 2, 4, 1, 4, 2], [4, 1, 1, 1, 2, 4, 1, 2, 2, 4, 2, 3, 1, 1, 2, 1],
                                     [4, 2, 1, 1, 2, 2, 4, 4, 1, 3, 2, 2, 3, 4, 1, 1], [3, 3, 1, 2, 3, 2, 3, 4, 1, 2, 4, 2, 4, 4, 4, 4], [4, 3, 2, 1, 2, 1, 2, 2, 4, 4, 3, 3, 1, 3, 1, 3],
                                     [3, 2, 3, 4, 1, 1, 3, 1, 2, 3, 2, 2, 3, 3, 4, 1], [1, 4, 2, 2, 1, 1, 1, 3, 2, 3, 1, 4, 2, 4, 2, 2], [1, 3, 2, 2, 4, 3, 3, 3, 1, 4, 2, 3, 4, 2, 3, 2],
                                     [4, 4, 4, 1, 4, 4, 1, 2, 3, 2, 3, 4, 3, 4, 3, 4], [1, 2, 1, 3, 3, 1, 3, 4, 4, 4, 2, 1, 3, 3, 4, 4], [2, 2, 3, 3, 1, 4, 1, 2, 4, 3, 3, 4, 4, 1, 4, 1],
                                     [4, 2, 1, 2, 3, 4, 2, 4, 3, 3, 3, 1, 3, 3, 1, 4], [1, 2, 2, 2, 4, 3, 2, 1, 2, 4, 2, 1, 1, 2, 1, 3], [3, 1, 4, 1, 1, 4, 3, 4, 4, 4, 3, 3, 4, 2, 3, 4],
                                     [3, 2, 3, 3, 1, 2, 4, 4, 3, 2, 1, 3, 4, 3, 2, 4], [4, 1, 3, 3, 1, 4, 3, 4, 3, 2, 3, 3, 3, 1, 3, 2], [3, 2, 3, 2, 1, 4, 2, 4, 1, 3, 4, 2, 3, 2, 2, 3],
                                     [1, 3, 2, 4, 1, 1, 3, 3, 1, 3, 2, 4, 4, 1, 4, 1], [4, 3, 3, 2, 1, 2, 1, 2, 4, 4, 2, 4, 3, 3, 4, 4], [3, 1, 3, 3, 4, 2, 3, 4, 3, 3, 3, 1, 2, 3, 2, 1],
                                     [2, 1, 4, 1, 1, 1, 3, 3, 1, 1, 2, 3, 4, 4, 1, 2], [2, 4, 1, 1, 2, 1, 2, 4, 1, 3, 4, 2, 2, 2, 3, 2], [1, 4, 1, 3, 3, 4, 1, 1, 1, 4, 1, 2, 1, 3, 4, 4],
                                     [3, 1, 1, 3, 3, 3, 4, 1, 4, 4, 2, 2, 3, 2, 1, 3], [2, 4, 3, 1, 3, 2, 1, 2, 4, 2, 4, 1, 4, 1, 4, 4], [2, 4, 4, 1, 4, 4, 1, 1, 1, 3, 3, 2, 2, 3, 4, 1],
                                     [4, 3, 1, 2, 3, 3, 4, 4, 4, 3, 1, 2, 3, 4, 2, 3], [2, 3, 2, 2, 1, 3, 3, 3, 2, 1, 2, 1, 4, 4, 4, 2], [3, 4, 4, 3, 1, 1, 1, 1, 1, 2, 2, 1, 3, 2, 4, 1],
                                     [4, 1, 1, 1, 2, 2, 2, 3, 2, 1, 2, 2, 3, 1, 4, 2], [2, 3, 1, 1, 2, 1, 2, 4, 4, 4, 3, 1, 1, 2, 1, 2], [3, 3, 2, 1, 1, 2, 3, 4, 3, 1, 3, 3, 4, 4, 2, 1],
                                     [3, 2, 3, 1, 4, 1, 1, 4, 4, 4, 4, 2, 4, 1, 2, 1], [1, 1, 2, 4, 1, 1, 3, 2, 4, 2, 2, 2, 4, 4, 4, 1], [1, 2, 4, 3, 2, 1, 4, 4, 4, 1, 4, 4, 3, 4, 3, 3],
                                     [4, 2, 3, 1, 3, 3, 4, 4, 4, 1, 2, 3, 4, 1, 2, 4], [1, 3, 1, 1, 4, 2, 3, 2, 2, 2, 3, 3, 4, 3, 4, 3], [4, 3, 4, 1, 2, 2, 2, 3, 4, 2, 4, 4, 2, 3, 1, 1],
                                     [2, 2, 2, 1, 2, 1, 2, 3, 1, 1, 4, 1, 3, 4, 1, 1], [1, 1, 4, 2, 1, 1, 1, 4, 4, 1, 2, 4, 3, 1, 1, 1], [3, 2, 3, 2, 1, 2, 3, 2, 2, 2, 4, 3, 4, 4, 3, 2],
                                     [3, 4, 2, 2, 1, 1, 4, 3, 3, 3, 2, 4, 3, 2, 3, 4], [2, 2, 1, 2, 3, 4, 3, 4, 1, 4, 4, 4, 3, 2, 3, 2], [1, 3, 1, 1, 4, 1, 4, 4, 3, 3, 1, 2, 3, 1, 2, 3],
                                     [2, 1, 2, 2, 4, 1, 1, 2, 1, 3, 1, 3, 4, 4, 3, 1], [1, 3, 3, 1, 4, 3, 4, 3, 3, 3, 2, 4, 4, 3, 4, 1], [3, 2, 1, 3, 2, 3, 2, 4, 3, 2, 1, 4, 4, 3, 3, 2],
                                     [1, 1, 4, 4, 4, 3, 1, 3, 2, 2, 3, 3, 3, 4, 3, 1], [4, 2, 2, 1, 4, 1, 2, 2, 4, 2, 3, 3, 2, 4, 2, 4], [3, 2, 2, 3, 1, 3, 1, 2, 2, 2, 1, 1, 2, 4, 3, 1],
                                     [1, 3, 3, 2, 4, 1, 4, 2, 4, 1, 1, 1, 3, 2, 2, 1], [3, 3, 3, 3, 1, 4, 3, 1, 3, 1, 3, 2, 2, 3, 3, 4], [2, 2, 4, 1, 3, 2, 1, 1, 2, 4, 2, 1, 1, 2, 3, 1],
                                     [4, 1, 1, 3, 3, 4, 2, 1, 2, 1, 3, 3, 4, 1, 1, 2], [2, 4, 4, 1, 3, 3, 1, 3, 3, 3, 4, 2, 4, 4, 4, 2], [3, 3, 1, 1, 4, 2, 1, 1, 4, 1, 2, 1, 1, 2, 3, 1],
                                     [1, 2, 4, 4, 2, 3, 4, 4, 4, 3, 3, 1, 4, 1, 3, 4], [3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 2, 1, 1, 3, 1, 1], [3, 3, 3, 2, 4, 4, 2, 2, 4, 2, 1, 2, 3, 2, 2, 1],
                                     [2, 1, 2, 2, 1, 2, 4, 4, 2, 1, 2, 3, 4, 2, 2, 1], [4, 4, 4, 2, 1, 2, 2, 3, 2, 1, 2, 3, 1, 2, 4, 3], [4, 4, 1, 3, 3, 4, 2, 2, 2, 3, 2, 4, 2, 1, 3, 2],
                                     [4, 3, 1, 3, 1, 2, 3, 1, 3, 1, 4, 4, 1, 4, 4, 1], [1, 3, 3, 1, 3, 2, 2, 4, 3, 4, 2, 1, 2, 4, 1, 3], [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 3, 2, 3],
                                     [4, 4, 2, 3, 3, 3, 2, 3, 4, 1, 3, 2, 3, 4, 3, 3], [3, 3, 4, 1, 1, 2, 1, 4, 2, 1, 3, 1, 2, 1, 2, 3], [1, 1, 2, 2, 2, 2, 3, 2, 4, 4, 2, 1, 4, 3, 2, 3],
                                     [2, 4, 1, 3, 4, 2, 3, 1, 2, 3, 4, 4, 4, 3, 2, 4], [4, 4, 1, 3, 1, 2, 1, 4, 3, 3, 1, 2, 1, 3, 2, 2], [3, 1, 4, 3, 1, 3, 1, 3, 3, 1, 1, 3, 2, 1, 3, 2],
                                     [4, 1, 4, 4, 2, 2, 1, 2, 4, 4, 2, 2, 1, 2, 2, 2], [4, 2, 1, 1, 2, 3, 4, 1, 4, 4, 3, 1, 1, 1, 4, 4], [4, 3, 4, 1, 2, 3, 4, 3, 2, 3, 3, 2, 1, 1, 2, 4],
                                     [2, 1, 3, 1, 3, 1, 3, 1, 1, 3, 3, 3, 3, 3, 1, 1], [2, 1, 3, 1, 1, 2, 1, 3, 2, 3, 4, 3, 3, 3, 3, 1], [1, 2, 2, 2, 2, 2, 3, 2, 1, 2, 4, 4, 2, 4, 3, 3],
                                     [1, 1, 1, 4, 2, 4, 2, 3, 3, 2, 3, 1, 1, 4, 2, 1], [2, 3, 1, 4, 3, 3, 1, 3, 1, 1, 1, 2, 4, 2, 3, 2], [4, 1, 4, 2, 4, 1, 3, 4, 2, 1, 2, 2, 2, 4, 3, 2],
                                     [3, 1, 4, 2, 1, 3, 2, 1, 3, 4, 4, 2, 3, 1, 2, 4], [4, 4, 3, 2, 1, 1, 3, 2, 2, 4, 2, 4, 1, 4, 2, 2], [2, 3, 2, 3, 1, 3, 4, 1, 1, 1, 3, 3, 3, 3, 2, 4],
                                     [3, 3, 3, 1, 2, 4, 1, 4, 1, 1, 3, 1, 3, 2, 1, 1], [3, 2, 4, 1, 1, 1, 1, 2, 1, 3, 4, 3, 3, 2, 1, 1], [4, 1, 1, 4, 1, 4, 3, 4, 3, 4, 2, 3, 1, 3, 2, 2]])
        )
        self.assertEqual(
            18,
            Solution().minCost(grid=[
                [3, 4, 3],
                [2, 2, 2],
                [2, 1, 1],
                [4, 3, 2],
                [2, 1, 4],
                [2, 4, 1],
                [3, 3, 3],
                [1, 4, 2],
                [2, 2, 1],
                [2, 1, 1],
                [3, 3, 1],
                [4, 1, 4],
                [2, 1, 4],
                [3, 2, 2],
                [3, 3, 1],
                [4, 4, 1],
                [1, 2, 2],
                [1, 1, 1],
                [1, 3, 4],
                [1, 2, 1],
                [2, 2, 4],
                [2, 1, 3],
                [1, 2, 1],
                [4, 3, 2],
                [3, 3, 4],
                [2, 2, 1],
                [3, 4, 3],
                [4, 2, 3],
                [4, 4, 4]
            ])
        )
        self.assertEqual(
            3,
            Solution().minCost(grid=[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]])
        )
        self.assertEqual(
            0,
            Solution().minCost(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]])
        )
        self.assertEqual(
            1,
            Solution().minCost(grid=[[1, 2], [4, 3]])
        )
        self.assertEqual(
            3,
            Solution().minCost(grid=[[2, 2, 2], [2, 2, 2]])
        )
        self.assertEqual(
            0,
            Solution().minCost(grid=[[4]])
        )
