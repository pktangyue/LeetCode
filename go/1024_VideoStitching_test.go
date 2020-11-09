package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestVideoStitching(t *testing.T) {
	assert.Equal(t,
		-1,
		videoStitching([][]int{
			{8, 10}, {17, 39}, {18, 19}, {8, 16}, {13, 35}, {33, 39}, {11, 19}, {18, 35},
		}, 20),
	)
	assert.Equal(t,
		3,
		videoStitching([][]int{
			{0, 1}, {6, 8}, {0, 2}, {5, 6}, {0, 4}, {0, 3}, {6, 7}, {1, 3}, {4, 7}, {1, 4}, {2, 5}, {2, 6}, {3, 4}, {4, 5}, {5, 7}, {6, 9},
		}, 9),
	)
	assert.Equal(t,
		3,
		videoStitching([][]int{
			{0, 2}, {4, 6}, {8, 10}, {1, 9}, {1, 5}, {5, 9},
		}, 10),
	)
	assert.Equal(t,
		-1,
		videoStitching([][]int{
			{0, 1}, {1, 2},
		}, 5),
	)
	assert.Equal(t,
		2,
		videoStitching([][]int{
			{0, 4}, {2, 8},
		}, 5),
	)
}
