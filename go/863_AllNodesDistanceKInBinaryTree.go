package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func distanceK(root *TreeNode, target *TreeNode, K int) []int {
	ret := make([]int, 0)
	var dfs func(node *TreeNode) int
	var addChildren func(node *TreeNode, dist int)
	dfs = func(node *TreeNode) (dist int) {
		// 计算出node距离target的距离, -1表示不是node的子节点
		if node == nil {
			return -1
		}
		if node.Val == target.Val {
			addChildren(node, dist)
			return dist
		}
		if l := dfs(node.Left); l != -1 {
			// l 为 node.Left 到 target 的距离
			dist = l + 1
			if dist == K {
				// node 本身距离 target 为 K
				ret = append(ret, node.Val)
			} else if dist < K {
				// node 本身距离target 小于K的情况下，node 距离为 dist，那么 node.Right 距离为 dist+1
				addChildren(node.Right, dist+1)
			}
			return dist
		}
		// 右边节点逻辑通上
		if r := dfs(node.Right); r != -1 {
			dist = r + 1
			if dist == K {
				ret = append(ret, node.Val)
			} else if dist < K {
				addChildren(node.Left, dist+1)
			}
			return dist
		}
		return -1
	}
	// 遍历 node 的子节点，如果距离为 K，则是一个合法值
	addChildren = func(node *TreeNode, dist int) {
		if node == nil {
			return
		}
		if dist == K {
			ret = append(ret, node.Val)
			return
		}
		dist++
		addChildren(node.Left, dist)
		addChildren(node.Right, dist)
	}
	dfs(root)
	return ret
}
