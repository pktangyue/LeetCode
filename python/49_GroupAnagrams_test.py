import unittest


class TestSolution(unittest.TestCase):

    def test_groupAnagrams(self):
        Solution = __import__('49_GroupAnagrams').Solution
        self.assertEqual(
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        )
