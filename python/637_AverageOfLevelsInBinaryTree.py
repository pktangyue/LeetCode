# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from models import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.amount = []
        self.count = []
        self.dfs(root, 0)
        return [x / y for x, y in zip(self.amount, self.count)]

    def dfs(self, node: TreeNode, depth: int):
        if depth == len(self.amount):
            self.amount.append(node.val)
            self.count.append(1)
        else:
            self.amount[depth] += node.val
            self.count[depth] += 1
        if node.left:
            self.dfs(node.left, depth + 1)
        if node.right:
            self.dfs(node.right, depth + 1)
