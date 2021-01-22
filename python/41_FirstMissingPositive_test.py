import unittest


class TestSolution(unittest.TestCase):

    def test_firstMissingPositive(self):
        Solution = __import__('41_FirstMissingPositive').Solution
        self.assertEqual(
            3,
            Solution().firstMissingPositive([1, 2, 0])
        )
        self.assertEqual(
            2,
            Solution().firstMissingPositive([3, 4, -1, 1])
        )
        self.assertEqual(
            1,
            Solution().firstMissingPositive([7, 8, 9, 11, 12])
        )
