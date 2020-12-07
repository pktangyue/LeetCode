package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCheckPerfectNumber(t *testing.T) {
	assert.Equal(t,
		true,
		checkPerfectNumber(28),
	)
	assert.Equal(t,
		true,
		checkPerfectNumber(6),
	)
	assert.Equal(t,
		true,
		checkPerfectNumber(496),
	)
	assert.Equal(t,
		true,
		checkPerfectNumber(8128),
	)
	assert.Equal(t,
		false,
		checkPerfectNumber(2),
	)
}
