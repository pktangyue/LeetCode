import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_averageOfLevels(self):
        Solution = __import__('637_AverageOfLevelsInBinaryTree').Solution
        self.assertEqual(
            [3, 14.5, 11],
            Solution().averageOfLevels(TreeNode.fromArray([3, 9, 20, 15, 7]))
        )
