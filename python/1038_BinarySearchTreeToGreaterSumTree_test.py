import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_bstToGst(self):
        Solution = __import__('1038_BinarySearchTreeToGreaterSumTree').Solution
        self.assertEqual(
            [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8],
            TreeNode.toArray(
                Solution().bstToGst(TreeNode.fromArray([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]))
            )
        )
        self.assertEqual(
            [1, None, 1],
            TreeNode.toArray(
                Solution().bstToGst(TreeNode.fromArray([0, None, 1]))
            )
        )
        self.assertEqual(
            [3, 3, 2],
            TreeNode.toArray(
                Solution().bstToGst(TreeNode.fromArray([1, 0, 2]))
            )
        )
        self.assertEqual(
            [7, 9, 4, 10],
            TreeNode.toArray(
                Solution().bstToGst(TreeNode.fromArray([3, 2, 4, 1]))
            )
        )
