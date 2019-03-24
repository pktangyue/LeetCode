package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestCheckInclusion(t *testing.T) {
    assert.Equal(t,
        true,
        checkInclusion("abb", "eidbbaooo"),
    )
    assert.Equal(t,
        true,
        checkInclusion("ab", "eidbaooo"),
    )
    assert.Equal(t,
        false,
        checkInclusion("ab", "eidboaoo"),
    )
    assert.Equal(t,
        false,
        checkInclusion("abb", "eidbaoo"),
    )
    assert.Equal(t,
        false,
        checkInclusion("hello", "ooolleoooleh"),
    )
    assert.Equal(t,
        true,
        checkInclusion("ab", "ab"),
    )
}
