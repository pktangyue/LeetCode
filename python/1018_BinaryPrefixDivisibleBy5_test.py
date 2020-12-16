import unittest


class TestSolution(unittest.TestCase):

    def test_PrefixesDivBy5(self):
        Solution = __import__('1018_BinaryPrefixDivisibleBy5').Solution
        self.assertEqual(
            [True, False, False],
            Solution().prefixesDivBy5([0, 1, 1])
        )
        self.assertEqual(
            [False, False, False],
            Solution().prefixesDivBy5([1, 1, 1])
        )
        self.assertEqual(
            [True, False, False, False, True, False],
            Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1])
        )
        self.assertEqual(
            [False, False, False, False, False],
            Solution().prefixesDivBy5([1, 1, 1, 0, 1])
        )
