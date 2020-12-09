package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinCost(t *testing.T) {
	assert.Equal(t,
		16,
		minCost(7, []int{1, 3, 4, 5}),
	)
	assert.Equal(t,
		22,
		minCost(9, []int{5, 6, 1, 4, 2}),
	)
	assert.Equal(t,
		71,
		minCost(20, []int{1, 14, 18, 6, 17, 8, 10, 4, 13, 16, 7}),
	)
	assert.Equal(t,
		92,
		minCost(30, []int{18, 15, 13, 7, 5, 26, 25, 29}),
	)
}
