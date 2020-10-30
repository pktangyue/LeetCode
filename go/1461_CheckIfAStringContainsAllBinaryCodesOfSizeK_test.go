package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHasAllCodes(t *testing.T) {
	assert.Equal(t,
		true,
		hasAllCodes("00110110", 2),
	)
	assert.Equal(t,
		true,
		hasAllCodes("00110", 2),
	)
	assert.Equal(t,
		true,
		hasAllCodes("0110", 1),
	)
	assert.Equal(t,
		false,
		hasAllCodes("0110", 2),
	)
	assert.Equal(t,
		false,
		hasAllCodes("0000000001011100", 4),
	)
}
