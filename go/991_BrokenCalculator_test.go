package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestBrokenCalc(t *testing.T) {
	assert.Equal(t,
		2,
		brokenCalc(2, 3),
	)
	assert.Equal(t,
		2,
		brokenCalc(5, 8),
	)
	assert.Equal(t,
		3,
		brokenCalc(3, 10),
	)
	assert.Equal(t,
		1023,
		brokenCalc(1024, 1),
	)
	assert.Equal(t,
		257,
		brokenCalc(511, 1024),
	)
}
