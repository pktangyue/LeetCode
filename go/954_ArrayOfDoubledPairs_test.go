package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCanReorderDoubled(t *testing.T) {
	assert.Equal(t,
		false,
		canReorderDoubled([]int{3, 1, 3, 6}),
	)
	assert.Equal(t,
		false,
		canReorderDoubled([]int{2, 1, 2, 6}),
	)
	assert.Equal(t,
		true,
		canReorderDoubled([]int{4, -2, 2, -4}),
	)
	assert.Equal(t,
		false,
		canReorderDoubled([]int{1, 2, 4, 16, 8, 4}),
	)
	assert.Equal(t,
		false,
		canReorderDoubled([]int{1, -1, 0, 0}),
	)
	assert.Equal(t,
		false,
		canReorderDoubled([]int{-5, -2}),
	)
}
