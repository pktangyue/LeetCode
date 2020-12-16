import unittest


class TestSolution(unittest.TestCase):

    def test_Combine(self):
        Solution = __import__('77_Combinations').Solution
        self.assertEqual(
            [
                [1, 2],
                [1, 3],
                [2, 3],
                [1, 4],
                [2, 4],
                [3, 4],
            ],
            Solution().combine(4, 2)
        )
        self.assertEqual(
            [[1]],
            Solution().combine(1, 1)
        )
