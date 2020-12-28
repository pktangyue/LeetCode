import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_flipEquiv(self):
        Solution = __import__('951_FlipEquivalentBinaryTrees').Solution
        self.assertEqual(
            False,
            Solution().flipEquiv(
                TreeNode.fromArray([6, 1, 0]),
                TreeNode.fromArray([6, None, 1])
            )
        )
        self.assertEqual(
            True,
            Solution().flipEquiv(
                TreeNode.fromArray([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
                TreeNode.fromArray([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])
            )
        )
        self.assertEqual(
            True,
            Solution().flipEquiv(
                TreeNode.fromArray([]),
                TreeNode.fromArray([])
            )
        )
        self.assertEqual(
            False,
            Solution().flipEquiv(
                TreeNode.fromArray([]),
                TreeNode.fromArray([1])
            )
        )
        self.assertEqual(
            False,
            Solution().flipEquiv(
                TreeNode.fromArray([0, None, 1]),
                TreeNode.fromArray([])
            )
        )
        self.assertEqual(
            True,
            Solution().flipEquiv(
                TreeNode.fromArray([0, None, 1]),
                TreeNode.fromArray([0, 1])
            )
        )
