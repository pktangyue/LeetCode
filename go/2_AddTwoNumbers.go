package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    result := l1
    carry := 0
    for true {
        // 没有了数据跳出循环
        if l1 == nil {
            break
        }
        // 把 l2 加进到 l1
        if l2 != nil {
            l1.Val += l2.Val
            l2 = l2.Next
        }
        // 加上之前的进位
        if carry == 1 {
            l1.Val += 1
            carry = 0
        }
        // 如果大于等于10，暂存到进位
        if l1.Val >= 10 {
            carry = 1
            l1.Val -= 10
        }
        // l1 没有剩余数据，需要查看 l2 和 carry 是否还有数据
        if l1.Next == nil {
            if l2 != nil {
                // l2 还有数据，把 l2 接上, 并把 l2 置为 nil
                l1.Next, l2 = l2, nil
            } else if carry == 1 {
                // 剩余进位还有值，但没有已有Node，需要新建一个node
                l1.Next = &ListNode{0, nil}
            }
        }
        // 处理剩余数据，可能为nil
        l1 = l1.Next
    }
    return result
}
