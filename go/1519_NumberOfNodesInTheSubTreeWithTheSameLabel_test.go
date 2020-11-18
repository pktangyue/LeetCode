package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCountSubTrees(t *testing.T) {
	assert.Equal(t,
		[]int{1, 1, 2, 1},
		countSubTrees(4, [][]int{
			{0, 2}, {0, 3}, {1, 2},
		}, "aeed"),
	)
	assert.Equal(t,
		[]int{6, 5, 4, 1, 3, 2, 1},
		countSubTrees(7, [][]int{
			{0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6},
		}, "aaabaaa"),
	)
	assert.Equal(t,
		[]int{2, 1, 1, 1, 1, 1, 1},
		countSubTrees(7, [][]int{
			{0, 1}, {0, 2}, {1, 4}, {1, 5}, {2, 3}, {2, 6},
		}, "abaedcd"),
	)
	assert.Equal(t,
		[]int{4, 2, 1, 1},
		countSubTrees(4, [][]int{
			{0, 1}, {1, 2}, {0, 3},
		}, "bbbb"),
	)
	assert.Equal(t,
		[]int{3, 2, 1, 1, 1},
		countSubTrees(5, [][]int{
			{0, 1}, {0, 2}, {1, 3}, {0, 4},
		}, "aabab"),
	)
	assert.Equal(t,
		[]int{1, 2, 1, 1, 2, 1},
		countSubTrees(6, [][]int{
			{0, 1}, {0, 2}, {1, 3}, {3, 4}, {4, 5},
		}, "cbabaa"),
	)
}
