# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from models import TreeNode


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 都为空节点，表示一致，返回True
        if not root1 and not root2:
            return True
        # 一个为空，一个不为空，返回False
        if (root1 and not root2) or (root2 and not root1):
            return False
        if root1.val != root2.val:
            return False
        a = self.flipEquiv(root1.left, root2.left)
        b = self.flipEquiv(root1.right, root2.right)
        c = self.flipEquiv(root1.left, root2.right)
        d = self.flipEquiv(root1.right, root2.left)
        return (a and b) or (c and d)
