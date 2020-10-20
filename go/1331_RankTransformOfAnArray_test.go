package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestArrayRankTransform(t *testing.T) {
	assert.Equal(t,
		[]int{4, 1, 2, 3},
		arrayRankTransform([]int{40, 10, 20, 30}),
	)
	assert.Equal(t,
		[]int{1, 1, 1},
		arrayRankTransform([]int{100, 100, 100}),
	)
	assert.Equal(t,
		[]int{5, 3, 4, 2, 8, 6, 7, 1, 3},
		arrayRankTransform([]int{37, 12, 28, 9, 100, 56, 80, 5, 12}),
	)
}
