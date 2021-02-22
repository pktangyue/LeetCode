import unittest


class TestSolution(unittest.TestCase):

    def test_reverseWords(self):
        Solution = __import__('557_ReverseWordsInAStringIII').Solution
        self.assertEqual(
            "s'teL ekat edoCteeL tsetnoc",
            Solution().reverseWords("Let's take LeetCode contest")
        )
