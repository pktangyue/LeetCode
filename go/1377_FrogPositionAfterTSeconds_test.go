package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFrogPosition(t *testing.T) {
	assert.Equal(t,
		0.16666666666666666,
		frogPosition(7, [][]int{
			{1, 2}, {1, 3}, {1, 7}, {2, 4}, {2, 6}, {3, 5},
		}, 2, 4),
	)
	assert.Equal(t,
		0.3333333333333333,
		frogPosition(7, [][]int{
			{1, 2}, {1, 3}, {1, 7}, {2, 4}, {2, 6}, {3, 5},
		}, 1, 7),
	)
	assert.Equal(t,
		0.00000,
		frogPosition(8, [][]int{
			{2, 1}, {3, 2}, {4, 1}, {5, 1}, {6, 4}, {7, 1}, {8, 7},
		}, 7, 7),
	)
	assert.Equal(t,
		1.00000,
		frogPosition(3, [][]int{
			{2, 1}, {3, 2},
		}, 1, 2),
	)
	assert.Equal(t,
		0.16666666666666666,
		frogPosition(7, [][]int{
			{1, 2}, {1, 3}, {1, 7}, {2, 4}, {2, 6}, {3, 5},
		}, 20, 6),
	)
}
