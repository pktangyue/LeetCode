import unittest


class TestSolution(unittest.TestCase):

    def test_LengthOfLongestSubstring(self):
        Solution = __import__('71_SimplifyPath').Solution
        self.assertEqual(
            "/home",
            Solution().simplifyPath("/home/"),
        )
        self.assertEqual(
            "/",
            Solution().simplifyPath("/../"),
        )
        self.assertEqual(
            "/home/foo",
            Solution().simplifyPath("/home//foo/"),
        )
        self.assertEqual(
            "/c",
            Solution().simplifyPath("/a/./b/../../c/"),
        )
        self.assertEqual(
            "/c",
            Solution().simplifyPath("/a/../../b/../c//.//"),
        )
        self.assertEqual(
            "/a/b/c",
            Solution().simplifyPath("/a//b////c/d//././/.."),
        )
