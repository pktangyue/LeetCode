import unittest


class TestSolution(unittest.TestCase):

    def test_TwoSum(self):
        Solution = __import__('1202_SmallestStringWithSwaps').Solution
        self.assertEqual(
            "bacd",
            Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]])
        )
        self.assertEqual(
            "abcd",
            Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]])
        )
        self.assertEqual(
            "abc",
            Solution().smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]])
        )
