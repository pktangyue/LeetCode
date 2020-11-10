package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCalculateMinimumHP(t *testing.T) {
	assert.Equal(t,
		7,
		calculateMinimumHP([][]int{
			{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5},
		}),
	)
}
