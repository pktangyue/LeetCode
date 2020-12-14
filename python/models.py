from __future__ import annotations

from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.val == other.val and self.next == other.next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromArray(cls, arr: List[Optional[int]]) -> Optional[TreeNode]:
        if len(arr) == 0:
            return None

        def dfs(i: int) -> Optional[TreeNode]:
            if not arr[i]:
                return None
            root = cls(arr[i])
            if 2 * i + 1 < len(arr):
                root.left = dfs(2 * i + 1)
            if 2 * i + 2 < len(arr):
                root.right = dfs(2 * i + 2)
            return root

        return dfs(0)
