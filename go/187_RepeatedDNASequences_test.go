package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindRepeatedDnaSequences(t *testing.T) {
	assert.Equal(t,
		[]string{"AAAAACCCCC", "CCCCCAAAAA"},
		findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"),
	)
	assert.Equal(t,
		[]string{"AAAAAAAAAA"},
		findRepeatedDnaSequences("AAAAAAAAAAAAA"),
	)
}
