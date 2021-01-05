# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from models import TreeNode


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0
        self.dfs(root)
        return root

    def dfs(self, node: TreeNode):
        if node.right:
            self.dfs(node.right)
        self.total += node.val
        node.val = self.total
        if node.left:
            self.dfs(node.left)
