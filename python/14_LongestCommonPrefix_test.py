import unittest


class TestTestSolution(unittest.TestCase):

    def test_TwoSum(self):
        Solution = __import__('14_LongestCommonPrefix').Solution
        self.assertEqual(
            "fl",
            Solution().longestCommonPrefix(["flower", "flow", "flight"])
        )
        self.assertEqual(
            "",
            Solution().longestCommonPrefix(["dog", "racecar", "car"])
        )
