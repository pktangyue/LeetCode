import unittest


class TestSolution(unittest.TestCase):

    def test_longestStrChain(self):
        Solution = __import__('1048_LongestStringChain').Solution
        self.assertEqual(
            2,
            Solution().longestStrChain(["a", "b", "ab", "bac"])
        )
        self.assertEqual(
            4,
            Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"])
        )
        self.assertEqual(
            5,
            Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"])
        )
