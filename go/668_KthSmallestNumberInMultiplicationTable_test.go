package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestFindKthNumber(t *testing.T) {
    assert.Equal(t,
        81,
        findKthNumber(9, 9, 81),
    )
    assert.Equal(t,
        3,
        findKthNumber(3, 1, 3),
    )
    assert.Equal(t,
        1,
        findKthNumber(3, 3, 1),
    )
    assert.Equal(t,
        3,
        findKthNumber(3, 3, 5),
    )
    assert.Equal(t,
        6,
        findKthNumber(2, 3, 6),
    )
    assert.Equal(t,
        126,
        findKthNumber(42, 34, 401),
    )
}
