import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_sortedArrayToBST(self):
        Solution = __import__('108_ConvertSortedArrayToBinarySearchTree').Solution
        self.assertEqual(
            [5, 3, 8],
            TreeNode.toArray(Solution().sortedArrayToBST([3, 5, 8]))
        )
        self.assertEqual(
            [0, -3, 9, -10, None, 5],
            TreeNode.toArray(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
        )
