import unittest


class TestSolution(unittest.TestCase):

    def test_countNumbersWithUniqueDigits(self):
        Solution = __import__('357_CountNumbersWithUniqueDigits').Solution
        self.assertEqual(
            91,
            Solution().countNumbersWithUniqueDigits(2)
        )
