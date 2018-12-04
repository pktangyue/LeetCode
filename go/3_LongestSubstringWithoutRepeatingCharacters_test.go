package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestLengthOfLongestSubstring(t *testing.T) {
    assert.Equal(t,
        3,
        lengthOfLongestSubstring("abcabcbb"),
    )
    assert.Equal(t,
        1,
        lengthOfLongestSubstring("bbbbb"),
    )
    assert.Equal(t,
        3,
        lengthOfLongestSubstring("pwwkew"),
    )
    assert.Equal(t,
        3,
        lengthOfLongestSubstring("aabaab!bb"),
    )
    assert.Equal(t,
        1,
        lengthOfLongestSubstring(" "),
    )
    assert.Equal(t,
        2,
        lengthOfLongestSubstring("au"),
    )
}
