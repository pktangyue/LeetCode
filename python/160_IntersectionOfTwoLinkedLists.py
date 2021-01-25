# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from models import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)

        # 让 A 保持为更长的，避免分两种情况
        if lenB > lenA:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        for i in range(lenA - lenB):
            headA = headA.next

        ret = None
        while headA:
            if not ret and headA == headB:
                ret = headA
            elif ret and headA != headB:
                ret = None

            headA = headA.next
            headB = headB.next

        return ret

    def getLen(self, head: ListNode):
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        return l
