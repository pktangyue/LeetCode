package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestValidTicTacToe(t *testing.T) {
    assert.Equal(t,
        false,
        validTicTacToe([]string{"O  ", "   ", "   "}),
    )
    assert.Equal(t,
        false,
        validTicTacToe([]string{"XOX", " X ", "   "}),
    )
    assert.Equal(t,
        false,
        validTicTacToe([]string{"XXX", "   ", "OOO"}),
    )
    assert.Equal(t,
        true,
        validTicTacToe([]string{"XOX", "O O", "XOX"}),
    )
    assert.Equal(t,
        true,
        validTicTacToe([]string{"XXX", "OOX", "OOX"}),
    )
    assert.Equal(t,
        false,
        validTicTacToe([]string{"XXX", "XOO", "OO "}),
    )
}
