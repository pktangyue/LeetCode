package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNetworkDelayTime(t *testing.T) {
	assert.Equal(t,
		3,
		networkDelayTime([][]int{
			{1, 2, 1}, {2, 3, 2}, {1, 3, 4},
		}, 3, 1),
	)
	assert.Equal(t,
		2,
		networkDelayTime([][]int{
			{2, 1, 1}, {2, 3, 1}, {3, 4, 1},
		}, 4, 2),
	)
	assert.Equal(t,
		59,
		networkDelayTime([][]int{
			{4, 2, 76}, {1, 3, 79}, {3, 1, 81}, {4, 3, 30}, {2, 1, 47}, {1, 5, 61}, {1, 4, 99}, {3, 4, 68}, {3, 5, 46}, {4, 1, 6}, {5, 4, 7}, {5, 3, 44}, {4, 5, 19}, {2, 3, 13}, {3, 2, 18}, {1, 2, 0}, {5, 1, 25}, {2, 5, 58}, {2, 4, 77}, {5, 2, 74},
		}, 5, 3),
	)
}
