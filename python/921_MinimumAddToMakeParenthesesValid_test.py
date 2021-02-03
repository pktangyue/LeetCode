import unittest


class TestSolution(unittest.TestCase):

    def test_minAddToMakeValid(self):
        Solution = __import__('921_MinimumAddToMakeParenthesesValid').Solution
        self.assertEqual(
            1,
            Solution().minAddToMakeValid("())")
        )
        self.assertEqual(
            3,
            Solution().minAddToMakeValid("(((")
        )
        self.assertEqual(
            0,
            Solution().minAddToMakeValid("()")
        )
        self.assertEqual(
            4,
            Solution().minAddToMakeValid("()))((")
        )
