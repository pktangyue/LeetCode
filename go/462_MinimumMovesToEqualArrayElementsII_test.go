package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestMinMoves2(t *testing.T) {
    assert.Equal(t,
        2,
        minMoves2([]int{1, 2, 3}),
    )
    assert.Equal(t,
        2,
        minMoves2([]int{3, 2, 1}),
    )
}
