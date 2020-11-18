package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinOperations(t *testing.T) {
	assert.Equal(t,
		2,
		minOperations([]string{"d1/", "d2/", "../", "d21/", "./"}),
	)
	assert.Equal(t,
		3,
		minOperations([]string{"d1/", "d2/", "./", "d3/", "../", "d31/"}),
	)
	assert.Equal(t,
		0,
		minOperations([]string{"d1/", "../", "../", "../"}),
	)
}
