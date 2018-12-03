# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.val == other.val and self.next == other.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = l1
        carry = 0
        while True:
            # 没有了数据跳出循环
            if l1 == None:
                break
            # 把 l2 加进到 l1
            if l2 != None:
                l1.val += l2.val
                l2 = l2.next
            # 加上之前的进位
            if carry == 1:
                l1.val += 1
                carry = 0
            # 如果大于等于10，暂存到进位
            if l1.val >= 10:
                carry = 1
                l1.val -= 10
            # l1 没有剩余数据，需要查看 l2 和 carry 是否还有数据
            if l1.next == None:
                if l2 != None:
                    # l2 还有数据，把 l2 接上, 并把 l2 置为 None
                    l1.next, l2 = l2, None
                elif carry == 1:
                    # 剩余进位还有值，但没有已有Node，需要新建一个node
                    l1.next = ListNode(0)

            # 处理剩余数据，可能为None
            l1 = l1.next

        return result
