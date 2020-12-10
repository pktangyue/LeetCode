package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestStrWithout3a3b(t *testing.T) {
	assert.Contains(t,
		[]string{"abb", "abb", "bab", "bba"},
		strWithout3a3b(1, 2),
	)
	assert.Contains(t,
		[]string{"aabaa"},
		strWithout3a3b(4, 1),
	)
}
