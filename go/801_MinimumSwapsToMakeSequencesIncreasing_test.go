package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinSwap(t *testing.T) {
	assert.Equal(t,
		1,
		minSwap([]int{1, 3, 5, 4}, []int{1, 2, 3, 7}),
	)
}
