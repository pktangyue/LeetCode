# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from models import TreeNode


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        m = {}

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            node.val += left_sum + right_sum
            if node.val in m:
                m[node.val] += 1
            else:
                m[node.val] = 1
            return node.val

        dfs(root)
        maxFreq = 0
        ret = []
        for k, v in m.items():
            if v > maxFreq:
                ret = [k]
                maxFreq = v
            elif v == maxFreq:
                ret.append(k)

        return ret
