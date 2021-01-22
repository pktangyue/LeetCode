import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_invertTree(self):
        Solution = __import__('226_InvertBinaryTree').Solution
        self.assertEqual(
            [4, 7, 2, 9, 6, 3, 1],
            TreeNode.toArray(Solution().invertTree(TreeNode.fromArray([4, 2, 7, 1, 3, 6, 9])))
        )
