import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_levelOrder(self):
        Solution = __import__('102_BinaryTreeLevelOrderTraversal').Solution
        self.assertEqual(
            [
                [3],
                [9, 20],
                [15, 7]
            ],
            Solution().levelOrder(TreeNode.fromArray([3, 9, 20, None, None, 15, 7]))
        )
