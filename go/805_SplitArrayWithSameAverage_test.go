package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSplitArraySameAverage(t *testing.T) {
	assert.Equal(t,
		false,
		splitArraySameAverage([]int{16, 19, 5, 0, 2, 3}),
	)
	assert.Equal(t,
		false,
		splitArraySameAverage([]int{1, 6, 1}),
	)
	assert.Equal(t,
		true,
		splitArraySameAverage([]int{10, 29, 13, 53, 33, 48, 76, 70, 5, 5}),
	)
	assert.Equal(t,
		true,
		splitArraySameAverage([]int{2, 0, 5, 6, 16, 12, 15, 12, 4}),
	)
	assert.Equal(t,
		true,
		splitArraySameAverage([]int{4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5}),
	)
	assert.Equal(t,
		false,
		splitArraySameAverage([]int{1, 2}),
	)
	assert.Equal(t,
		true,
		splitArraySameAverage([]int{1, 2, 3, 4, 5, 6, 7, 8}),
	)
}
