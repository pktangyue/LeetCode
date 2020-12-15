# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from models import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.path = []
        self.dfs(root, [])
        return self.path

    def dfs(self, root: TreeNode, paths: List[str]):
        paths.append(str(root.val))
        if not root.left and not root.right:
            self.path.append("->".join(paths))
            return
        if root.left:
            self.dfs(root.left, paths[:])
        if root.right:
            self.dfs(root.right, paths[:])
