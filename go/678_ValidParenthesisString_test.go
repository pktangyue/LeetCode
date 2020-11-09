package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCheckValidString(t *testing.T) {
	assert.Equal(t,
		true,
		checkValidString("()"),
	)
	assert.Equal(t,
		true,
		checkValidString("(*)"),
	)
	assert.Equal(t,
		true,
		checkValidString("(*))"),
	)
}
