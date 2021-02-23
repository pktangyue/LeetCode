import unittest


class TestSolution(unittest.TestCase):

    def test_letterCasePermutation(self):
        Solution = __import__('784_LetterCasePermutation').Solution
        self.assertEqual(
            ["a1b2", "a1B2", "A1b2", "A1B2"],
            Solution().letterCasePermutation(S="a1b2")
        )
        self.assertEqual(
            ["3z4", "3Z4"],
            Solution().letterCasePermutation(S="3z4")
        )
        self.assertEqual(
            ["12345"],
            Solution().letterCasePermutation(S="12345")
        )
        self.assertEqual(
            ["0"],
            Solution().letterCasePermutation(S="0")
        )
