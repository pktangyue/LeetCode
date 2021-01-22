import unittest


class TestSolution(unittest.TestCase):

    def test_wordBreak(self):
        Solution = __import__('139_WordBreak').Solution
        self.assertEqual(
            True,
            Solution().wordBreak(s="leetcode", wordDict=["leet", "code"])
        )
        self.assertEqual(
            True,
            Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
        )
        self.assertEqual(
            False,
            Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
        )
