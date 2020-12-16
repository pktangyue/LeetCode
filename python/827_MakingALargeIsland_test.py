import unittest


class TestSolution(unittest.TestCase):

    def test_LargestIsland(self):
        Solution = __import__('827_MakingALargeIsland').Solution
        self.assertEqual(
            15,
            Solution().largestIsland([
                [1, 0, 1, 0, 1],
                [0, 1, 1, 0, 1],
                [1, 1, 1, 0, 0],
                [1, 0, 1, 1, 1],
                [0, 0, 1, 1, 0]
            ])
        )
        self.assertEqual(
            4,
            Solution().largestIsland([[1, 1], [1, 0]])
        )
        self.assertEqual(
            3,
            Solution().largestIsland([[1, 0], [0, 1]])
        )
        self.assertEqual(
            4,
            Solution().largestIsland([[1, 1], [1, 1]])
        )
