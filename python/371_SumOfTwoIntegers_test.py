import unittest


class TestSolution(unittest.TestCase):

    def test_GetSum(self):
        Solution = __import__('371_SumOfTwoIntegers').Solution
        self.assertEqual(
            3,
            Solution().getSum(1, 2)
        )
        self.assertEqual(
            -3,
            Solution().getSum(-2, -1)
        )
        self.assertEqual(
            1,
            Solution().getSum(-2, 3)
        )
