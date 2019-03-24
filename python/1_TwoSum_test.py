import unittest


class TestSolution(unittest.TestCase):

    def test_TwoSum(self):
        Solution = __import__('1_TwoSum').Solution
        self.assertEqual(
            [0, 1],
            Solution().twoSum([2, 7, 11, 15], 9)
        )
