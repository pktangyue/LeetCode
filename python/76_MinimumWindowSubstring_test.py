import unittest


class TestSolution(unittest.TestCase):

    def test_minWindow(self):
        Solution = __import__('76_MinimumWindowSubstring').Solution
        self.assertEqual(
            "",
            Solution().minWindow("a", "aa")
        )
        self.assertEqual(
            "BANC",
            Solution().minWindow("ADOBECODEBANC", "ABC")
        )
        self.assertEqual(
            "a",
            Solution().minWindow("a", "a")
        )
