package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertionSortList(head *ListNode) *ListNode {
	var ret *ListNode
	ret, head, head.Next = head, head.Next, ret
	for head != nil {
		if ret.Val > head.Val {
			ret, head.Next, head = head, ret, head.Next
			continue
		}
		node := ret
		inserted := false
		for node.Next != nil {
			if node.Next.Val > head.Val {
				node.Next, head.Next, head = head, node.Next, head.Next
				inserted = true
				break
			} else {
				node = node.Next
			}
		}
		if !inserted {
			node.Next, head, head.Next = head, head.Next, node.Next
		}
	}
	return ret
}
