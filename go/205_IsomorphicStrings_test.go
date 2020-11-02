package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsIsomorphic(t *testing.T) {
	assert.Equal(t,
		false,
		isIsomorphic("ab", "aa"),
	)
	assert.Equal(t,
		true,
		isIsomorphic("egg", "add"),
	)
	assert.Equal(t,
		false,
		isIsomorphic("foo", "bar"),
	)
	assert.Equal(t,
		true,
		isIsomorphic("paper", "title"),
	)
}
