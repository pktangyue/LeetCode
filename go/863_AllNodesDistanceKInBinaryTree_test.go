package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDistanceK(t *testing.T) {
	assert.EqualValues(t,
		[]int{7, 4, 1},
		distanceK(&TreeNode{
			Val: 3,
			Left: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 6,
				},
				Right: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 7},
					Right: &TreeNode{Val: 4},
				},
			},
			Right: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 0},
				Right: &TreeNode{Val: 8},
			},
		}, &TreeNode{Val: 5}, 2),
	)
}
