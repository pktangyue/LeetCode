import unittest


class TestSolution(unittest.TestCase):

    def test_sumEvenAfterQueries(self):
        Solution = __import__('985_SumOfEvenNumbersAfterQueries').Solution
        self.assertEqual(
            [8, 6, 2, 4],
            Solution().sumEvenAfterQueries(A=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]])
        )
