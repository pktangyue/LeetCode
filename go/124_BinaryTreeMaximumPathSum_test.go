package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMaxPathSum(t *testing.T) {
	assert.Equal(t,
		49,
		maxPathSum(&TreeNode{
			Val: 5,
			Left: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val: 11,
					Left: &TreeNode{
						Val: 7,
					},
					Right: &TreeNode{
						Val: 2,
					},
				},
			},
			Right: &TreeNode{
				Val: 8,
				Left: &TreeNode{
					Val: 13,
					Right: &TreeNode{
						Val: 1,
					},
				},
				Right: &TreeNode{
					Val: 4,
				},
			},
		}),
	)
	assert.Equal(t,
		3,
		maxPathSum(&TreeNode{
			Val: 1,
			Left: &TreeNode{
				Val: -2,
				Left: &TreeNode{
					Val: 1,
					Left: &TreeNode{
						Val: -1,
					},
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
			Right: &TreeNode{
				Val: -3,
				Left: &TreeNode{
					Val: -2,
				},
			},
		}),
	)
	assert.Equal(t,
		6,
		maxPathSum(&TreeNode{
			Val: 1,
			Left: &TreeNode{
				Val: 2,
			},
			Right: &TreeNode{
				Val: 3,
			},
		}),
	)
	assert.Equal(t,
		42,
		maxPathSum(&TreeNode{
			Val: -10,
			Left: &TreeNode{
				Val: 9,
			},
			Right: &TreeNode{
				Val: 20,
				Left: &TreeNode{
					Val: 15,
				},
				Right: &TreeNode{
					Val: 7,
				},
			},
		}),
	)
	assert.Equal(t,
		-3,
		maxPathSum(&TreeNode{
			Val: -3,
		}),
	)
	assert.Equal(t,
		2,
		maxPathSum(&TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: -1,
			},
		}),
	)
}
