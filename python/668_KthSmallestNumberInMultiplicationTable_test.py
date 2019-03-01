import unittest


class TestSolution(unittest.TestCase):

    def test_findKthNumber(self):
        Solution = __import__('668_KthSmallestNumberInMultiplicationTable').Solution
        self.assertEqual(
            81,
            Solution().findKthNumber(9, 9, 81)
        )
        self.assertEqual(
            3,
            Solution().findKthNumber(3, 1, 3)
        )
        self.assertEqual(
            1,
            Solution().findKthNumber(3, 3, 1)
        )
        self.assertEqual(
            3,
            Solution().findKthNumber(3, 3, 5)
        )
        self.assertEqual(
            6,
            Solution().findKthNumber(2, 3, 6)
        )
        self.assertEqual(
            126,
            Solution().findKthNumber(42, 34, 401)
        )
