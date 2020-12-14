# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from models import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.ret = True

        def dfs(root: TreeNode, depth: int) -> int:
            left_depth = dfs(root.left, depth + 1) if root.left else depth
            right_depth = dfs(root.right, depth + 1) if root.right else depth

            if abs(left_depth - right_depth) > 1:
                self.ret = False
            return max(left_depth, right_depth)

        dfs(root, 0)
        return self.ret
