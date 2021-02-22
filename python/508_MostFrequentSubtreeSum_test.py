import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_findFrequentTreeSum(self):
        Solution = __import__('508_MostFrequentSubtreeSum').Solution
        self.assertEqual(
            [2, -3, 4],
            Solution().findFrequentTreeSum(TreeNode.fromArray([5, 2, -3]))
        )
        self.assertEqual(
            [2],
            Solution().findFrequentTreeSum(TreeNode.fromArray([5, 2, -5]))
        )
