package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSolveNQueens(t *testing.T) {
	assert.Equal(t,
		[][]string{
			{".Q..", "...Q", "Q...", "..Q."},
			{"..Q.", "Q...", "...Q", ".Q.."},
		},
		solveNQueens(4),
	)
}
