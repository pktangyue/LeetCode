package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSearchMatrix(t *testing.T) {
	assert.Equal(t,
		true,
		searchMatrix([][]int{
			{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 50},
		}, 3),
	)
	assert.Equal(t,
		false,
		searchMatrix([][]int{
			{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 50},
		}, 13),
	)
	assert.Equal(t,
		false,
		searchMatrix([][]int{}, 0),
	)
}
