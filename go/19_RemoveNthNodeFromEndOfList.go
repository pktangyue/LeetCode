package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    // l2 比 l1 先走 n 个元素，当 l2 到末尾的时候，删除 l1.Next 就可
    l1, l2 := head, head
    for i := 0; i < n; i++ {
        l2 = l2.Next
    }
    for {
        if l2 == nil {
            return l1.Next
        } else if l2.Next == nil {
            l1.Next = l1.Next.Next
            break
        } else {
            l1 = l1.Next
            l2 = l2.Next
        }
    }
    return head
}
