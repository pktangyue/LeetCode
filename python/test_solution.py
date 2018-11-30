import unittest


class TestTestSolution(unittest.TestCase):

    def test_TwoSum(self):
        TwoSumSolution = __import__('1_TwoSum').Solution
        self.assertEqual([0, 1], TwoSumSolution().twoSum([2, 7, 11, 15], 9))
