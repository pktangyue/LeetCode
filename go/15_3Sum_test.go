package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestThreeSum(t *testing.T) {
    assert.Equal(t,
        [][]int{
            {0, 0, 0},
        },
        threeSum([]int{0, 0, 0}),
    )
    assert.Equal(t,
        [][]int{
            {-1, -1, 2},
            {-1, 0, 1},
        },
        threeSum([]int{-1, 0, 1, 2, -1, -4}),
    )
}
