import unittest


class TestSolution(unittest.TestCase):

    def test_equalSubstring(self):
        Solution = __import__('1208_GetEqualSubstringsWithinBudget').Solution
        self.assertEqual(
            3,
            Solution().equalSubstring("abcd", "bcdf", 3)
        )
        self.assertEqual(
            1,
            Solution().equalSubstring("abcd", "cdef", 3)
        )
        self.assertEqual(
            1,
            Solution().equalSubstring("abcd", "acde", 0)
        )
