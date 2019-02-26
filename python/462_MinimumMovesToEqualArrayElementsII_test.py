import unittest


class TestSolution(unittest.TestCase):

    def test_MinMoves2(self):
        Solution = __import__('462_MinimumMovesToEqualArrayElementsII').Solution
        self.assertEqual(
            2,
            Solution().minMoves2([1, 2, 3])
        )
        self.assertEqual(
            2,
            Solution().minMoves2([3, 2, 1])
        )
