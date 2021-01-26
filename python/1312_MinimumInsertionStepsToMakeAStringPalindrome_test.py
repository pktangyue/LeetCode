import unittest


class TestSolution(unittest.TestCase):

    def test_minInsertions(self):
        Solution = __import__('1312_MinimumInsertionStepsToMakeAStringPalindrome').Solution
        self.assertEqual(
            2,
            Solution().minInsertions(s="mbadm")
        )
        self.assertEqual(
            1,
            Solution().minInsertions(s="acccccab")
        )
        self.assertEqual(
            0,
            Solution().minInsertions(s="zzazz")
        )
        self.assertEqual(
            5,
            Solution().minInsertions(s="leetcode")
        )
        self.assertEqual(
            0,
            Solution().minInsertions(s="g")
        )
        self.assertEqual(
            1,
            Solution().minInsertions(s="no")
        )
