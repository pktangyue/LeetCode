from __future__ import annotations

from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.val == other.val and self.next == other.next


class TreeNode:
    def __init__(self, val=0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromArray(cls, arr: List[Optional[int]]) -> Optional[TreeNode]:
        if len(arr) == 0:
            return None
        root = cls(arr.pop(0))
        nodes = [root]
        while arr:
            node = nodes.pop(0)
            left = arr.pop(0)
            if left is not None:
                node.left = cls(left)
                nodes.append(node.left)
            if arr:
                right = arr.pop(0)
                if right is not None:
                    node.right = cls(right)
                    nodes.append(node.right)
        return root

    @classmethod
    def toArray(cls, root: Optional[TreeNode]) -> List[Optional[int]]:
        ret = []
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            ret.append(node and node.val)
            if node:
                nodes.append(node.left)
                nodes.append(node.right)

        while ret and ret[-1] is None:
            del ret[-1]
        return ret
