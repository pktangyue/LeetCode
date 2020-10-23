package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRemoveDuplicateLetters(t *testing.T) {
	assert.Equal(t,
		"acdb",
		removeDuplicateLetters("cbacdcbc"),
	)
	assert.Equal(t,
		"abc",
		removeDuplicateLetters("bcabc"),
	)
	assert.Equal(t,
		"acdb",
		removeDuplicateLetters("cbacdcbc"),
	)
}
