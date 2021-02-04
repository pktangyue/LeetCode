import unittest

from models import TreeNode


class TestSolution(unittest.TestCase):

    def test_delNodes(self):
        Solution = __import__('1110_DeleteNodesAndReturnForest').Solution
        self.assertEqual(
            [[1, 2, None, 4], [6], [7]],
            [TreeNode.toArray(v) for v in Solution().delNodes(root=TreeNode.fromArray([1, 2, 3, 4, 5, 6, 7]), to_delete=[3, 5])]
        )
        self.assertEqual(
            [[1], [4]],
            [TreeNode.toArray(v) for v in Solution().delNodes(root=TreeNode.fromArray([1, 2, None, 4, 3]), to_delete=[2, 3])]
        )
