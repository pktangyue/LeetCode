import unittest


class TestSolution(unittest.TestCase):

    def test_MaxJumps(self):
        Solution = __import__('1340_JumpGameV').Solution
        self.assertEqual(
            4,
            Solution().maxJumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2),
        )
        self.assertEqual(
            1,
            Solution().maxJumps([3, 3, 3, 3, 3], 3),
        )
        self.assertEqual(
            7,
            Solution().maxJumps([7, 6, 5, 4, 3, 2, 1], 1),
        )
        self.assertEqual(
            2,
            Solution().maxJumps([7, 1, 7, 1, 7, 1], 2),
        )
        self.assertEqual(
            1,
            Solution().maxJumps([6, 6], 1),
        )
