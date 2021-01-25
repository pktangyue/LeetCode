import unittest

from models import ListNode


class TestSolution(unittest.TestCase):

    def test_getIntersectionNode(self):
        Solution = __import__('160_IntersectionOfTwoLinkedLists').Solution
        self.assertEqual(
            [8, 4, 5],
            ListNode.toArray(Solution().getIntersectionNode(ListNode.fromArray([4, 1, 8, 4, 5]), ListNode.fromArray([5, 6, 1, 8, 4, 5])))
        )
        self.assertEqual(
            [2, 4],
            ListNode.toArray(Solution().getIntersectionNode(ListNode.fromArray([1, 9, 1, 2, 4]), ListNode.fromArray([3, 2, 4])))
        )
        self.assertEqual(
            None,
            ListNode.toArray(Solution().getIntersectionNode(ListNode.fromArray([2, 6, 4]), ListNode.fromArray([1, 5])))
        )
