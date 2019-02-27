package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestFindMinArrowShots(t *testing.T) {
    assert.Equal(t,
        2,
        findMinArrowShots([][]int{{10, 16}, {2, 8}, {1, 6}, {7, 12}}),
    )
    assert.Equal(t,
        2,
        findMinArrowShots([][]int{{1, 3}, {1, 7}, {4, 10}, {8, 10}}),
    )
}
