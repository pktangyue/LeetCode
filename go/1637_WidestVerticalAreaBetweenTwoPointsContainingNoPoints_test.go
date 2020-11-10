package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMaxWidthOfVerticalArea(t *testing.T) {
	assert.Equal(t,
		1,
		maxWidthOfVerticalArea([][]int{
			{8, 7}, {9, 9}, {7, 4}, {9, 7},
		}),
	)
	assert.Equal(t,
		3,
		maxWidthOfVerticalArea([][]int{
			{3, 1}, {9, 0}, {1, 0}, {1, 4}, {5, 3}, {8, 8},
		}),
	)
}
