import unittest


class TestSolution(unittest.TestCase):

    def test_findMaxConsecutiveOnes(self):
        Solution = __import__('485_MaxConsecutiveOnes').Solution
        self.assertEqual(
            3,
            Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
        )
