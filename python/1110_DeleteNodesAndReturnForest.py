# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from models import TreeNode


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ret = []

        def dfs(node: TreeNode, hasParent: bool) -> bool:
            if not node:
                return False
            isDeleted = node.val in to_delete
            if not hasParent and not isDeleted:
                ret.append(node)

            leftIsDeleted = dfs(node.left, not isDeleted)
            if leftIsDeleted:
                node.left = None

            rightIsDeleted = dfs(node.right, not isDeleted)
            if rightIsDeleted:
                node.right = None

            return isDeleted

        dfs(root, False)
        return ret
