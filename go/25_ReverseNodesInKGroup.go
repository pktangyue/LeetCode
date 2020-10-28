package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseKGroup(head *ListNode, k int) *ListNode {
	var ret *ListNode
	// 记录ret的尾结点，省去重新遍历
	var tailNode *ListNode
	for head != nil {
		// 优先判断剩余数量是否大于等于k个
		if checkCount(head, k) {
			i := 0
			// 临时记录翻转后的尾结点
			tmpTail := head
			// 翻转k个node
			var reversed *ListNode
			for head != nil && i < k {
				reversed, head.Next, head = head, reversed, head.Next
				i++
			}
			// 初始化ret，否则直接更新尾结点的next
			if ret == nil {
				ret = reversed
			} else {
				if tailNode != nil {
					tailNode.Next = reversed
				}
			}
			// 更新尾结点
			tailNode = tmpTail
		} else {
			// 初始化ret，否则直接更新尾结点的next
			if tailNode != nil {
				tailNode.Next = head
			} else {
				ret = head
			}
			break
		}
	}
	return ret
}

func checkCount(head *ListNode, k int) bool {
	count := 0
	p := head
	for p != nil {
		count++
		p = p.Next
		if count >= k {
			return true
		}
	}
	return false
}
