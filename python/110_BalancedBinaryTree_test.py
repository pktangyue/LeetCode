import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_IsBalanced(self):
        Solution = __import__('110_BalancedBinaryTree').Solution
        # self.assertEqual(
        #     True,
        #     Solution().isBalanced(TreeNode.fromArray([3, 9, 20, None, None, 15, 7]))
        # )
        self.assertEqual(
            False,
            Solution().isBalanced(TreeNode.fromArray([1, 2, 2, 3, 3, None, None, 4, 4]))
        )
        self.assertEqual(
            True,
            Solution().isBalanced(TreeNode.fromArray([]))
        )
