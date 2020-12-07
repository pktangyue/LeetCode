package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindMinFibonacciNumbers(t *testing.T) {
	assert.Equal(t,
		2,
		findMinFibonacciNumbers(7),
	)
	assert.Equal(t,
		2,
		findMinFibonacciNumbers(10),
	)
	assert.Equal(t,
		3,
		findMinFibonacciNumbers(19),
	)
}
