import unittest


class TestSolution(unittest.TestCase):

    def test_LengthOfLongestSubstring(self):
        Solution = __import__('3_LongestSubstringWithoutRepeatingCharacters').Solution
        self.assertEqual(
            3,
            Solution().lengthOfLongestSubstring("abcabcbb")
        )
        self.assertEqual(
            1,
            Solution().lengthOfLongestSubstring("bbbbb")
        )
        self.assertEqual(
            3,
            Solution().lengthOfLongestSubstring("pwwkew")
        )
        self.assertEqual(
            3,
            Solution().lengthOfLongestSubstring("aabaab!bb")
        )
        self.assertEqual(
            1,
            Solution().lengthOfLongestSubstring(" ")
        )
        self.assertEqual(
            2,
            Solution().lengthOfLongestSubstring("au")
        )
