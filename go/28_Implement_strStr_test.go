package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestStrStr(t *testing.T) {
	assert.Equal(t,
		4,
		strStr("ababababac", "ababac"),
	)
	assert.Equal(t,
		2,
		strStr("hello", "ll"),
	)
	assert.Equal(t,
		-1,
		strStr("aaaaa", "bba"),
	)
	assert.Equal(t,
		0,
		strStr("", ""),
	)
}
