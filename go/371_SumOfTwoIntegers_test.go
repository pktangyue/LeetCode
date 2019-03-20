package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestGetSum(t *testing.T) {
    assert.Equal(t,
        3,
        getSum(1, 2),
    )
    assert.Equal(t,
        1,
        getSum(-2, 3),
    )
}
