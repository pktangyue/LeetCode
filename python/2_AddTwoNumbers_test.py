import unittest


class TestSolution(unittest.TestCase):

    def test_AddTwoNumbers(self):
        module = __import__('2_AddTwoNumbers')
        Solution = module.Solution
        ListNode = module.ListNode

        target = ListNode(7)
        target.next = ListNode(0)
        target.next.next = ListNode(8)
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        self.assertEqual(
            target,
            Solution().addTwoNumbers(l1, l2)
        )

        target = ListNode(7)
        target.next = ListNode(0)
        target.next.next = ListNode(0)
        target.next.next.next = ListNode(1)
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(5)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        self.assertEqual(
            target,
            Solution().addTwoNumbers(l1, l2)
        )

        target = ListNode(7)
        target.next = ListNode(0)
        target.next.next = ListNode(8)
        target.next.next.next = ListNode(1)
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(1)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        self.assertEqual(
            target,
            Solution().addTwoNumbers(l1, l2)
        )

        target = ListNode(7)
        target.next = ListNode(0)
        target.next.next = ListNode(8)
        target.next.next.next = ListNode(1)
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        l2.next.next.next = ListNode(1)
        self.assertEqual(
            target,
            Solution().addTwoNumbers(l1, l2)
        )
