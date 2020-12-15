import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_BinaryTreePaths(self):
        Solution = __import__('257_BinaryTreePaths').Solution
        self.assertEqual(
            ["1->2->5", "1->3"],
            Solution().binaryTreePaths(TreeNode(
                val=1,
                left=TreeNode(val=2, right=TreeNode(val=5)),
                right=TreeNode(val=3),
            ))
        )
