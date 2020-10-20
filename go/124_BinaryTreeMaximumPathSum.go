package main

import (
	"math"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxPathSum(root *TreeNode) int {
	max1, max2 := maxOfSubTree(root)
	if max1 > max2 {
		return max1
	}
	return max2
}

// 分别返回包含root节点的最大值，以及不包含root节点的最大值
func maxOfSubTree(root *TreeNode) (int, int) {
	if root == nil {
		return math.MinInt32, math.MinInt32
	}
	leftMaxWithRoot, leftMaxNoRoot := maxOfSubTree(root.Left)
	rightMaxWithRoot, rightMaxNoRoot := maxOfSubTree(root.Right)
	maxWithRoot, maxNoRoot := getMax(leftMaxWithRoot, root.Val, rightMaxWithRoot)
	if leftMaxNoRoot > maxNoRoot {
		maxNoRoot = leftMaxNoRoot
	}
	if rightMaxNoRoot > maxNoRoot {
		maxNoRoot = rightMaxNoRoot
	}
	return maxWithRoot, maxNoRoot
}

func getMax(left, root, right int) (int, int) {
	// 遍历六种情况，看哪个最大
	maxWithRoot := math.MinInt32
	maxNoRoot := math.MinInt32
	if left > maxNoRoot {
		maxNoRoot = left
	}
	if right > maxNoRoot {
		maxNoRoot = right
	}
	if root+right+left > maxNoRoot {
		maxNoRoot = root + right + left
	}
	if root > maxWithRoot {
		maxWithRoot = root
	}
	if root+left > maxWithRoot {
		maxWithRoot = root + left
	}
	if root+right > maxWithRoot {
		maxWithRoot = root + right
	}
	return maxWithRoot, maxNoRoot
}
