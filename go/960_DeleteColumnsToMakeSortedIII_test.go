package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinDeletionSize(t *testing.T) {
	assert.Equal(t,
		3,
		minDeletionSize([]string{"babca", "bbazb"}),
	)
	assert.Equal(t,
		4,
		minDeletionSize([]string{"edcba"}),
	)
	assert.Equal(t,
		0,
		minDeletionSize([]string{"ghi", "def", "abc"}),
	)
}
