package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCarPooling(t *testing.T) {
	assert.Equal(t,
		false,
		carPooling([][]int{
			{2, 1, 5}, {3, 3, 7},
		}, 4),
	)
	assert.Equal(t,
		true,
		carPooling([][]int{
			{2, 1, 5}, {3, 3, 7},
		}, 5),
	)
	assert.Equal(t,
		true,
		carPooling([][]int{
			{2, 1, 5}, {3, 5, 7},
		}, 3),
	)
	assert.Equal(t,
		true,
		carPooling([][]int{
			{3, 2, 7}, {3, 7, 9}, {8, 3, 9},
		}, 11),
	)
}
