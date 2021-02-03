# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from models import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        i = len(nums) // 2
        node = TreeNode(val=nums[i])
        node.left = self.sortedArrayToBST(nums[:i])
        node.right = self.sortedArrayToBST(nums[i + 1:])
        return node
