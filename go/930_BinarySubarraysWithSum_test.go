package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNumSubarraysWithSum(t *testing.T) {
	assert.Equal(t,
		4,
		numSubarraysWithSum([]int{1, 0, 1, 0, 1}, 2),
	)
	assert.Equal(t,
		15,
		numSubarraysWithSum([]int{0, 0, 0, 0, 0}, 0),
	)
	assert.Equal(t,
		2,
		numSubarraysWithSum([]int{1, 0, 1, 0, 1}, 0),
	)
}
