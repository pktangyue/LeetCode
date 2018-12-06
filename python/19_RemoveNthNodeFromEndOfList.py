# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # l2 比 l1 先走 n 个元素，当 l2 到末尾的时候，删除 l1.Next 就可
        l1 = l2 = head
        for i in range(n):
            l2 = l2.next

        while True:
            if l2 == None:
                return l1.next
            elif l2.next == None:
                l1.next = l1.next.next
                break
            else:
                l1 = l1.next
                l2 = l2.next

        return head
