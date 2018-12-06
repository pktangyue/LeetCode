import unittest

from models import ListNode


class TestSolution(unittest.TestCase):

    def test_RemoveNthFromEnd(self):
        module = __import__('19_RemoveNthNodeFromEndOfList')
        Solution = module.Solution

        target = ListNode(1)
        target.next = ListNode(2)
        target.next.next = ListNode(3)
        target.next.next.next = ListNode(5)
        l = ListNode(1)
        l.next = ListNode(2)
        l.next.next = ListNode(3)
        l.next.next.next = ListNode(4)
        l.next.next.next.next = ListNode(5)
        self.assertEqual(
            target,
            Solution().removeNthFromEnd(l, 2)
        )

        target = ListNode(2)
        l = ListNode(1)
        l.next = ListNode(2)
        self.assertEqual(
            target,
            Solution().removeNthFromEnd(l, 2)
        )

        l = ListNode(1)
        self.assertIsNone(
            Solution().removeNthFromEnd(l, 1)
        )
