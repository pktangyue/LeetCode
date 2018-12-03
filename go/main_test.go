package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestTwoSum(t *testing.T) {
    assert.Equal(t,
        []int{0, 1},
        twoSum([]int{2, 7, 11, 15}, 9),
    )
}

func TestAddTwoNumbers(t *testing.T) {
    assert.Equal(t,
        &ListNode{7, &ListNode{0, &ListNode{8, nil}}},
        addTwoNumbers(
            &ListNode{2, &ListNode{4, &ListNode{3, nil}}},
            &ListNode{5, &ListNode{6, &ListNode{4, nil}}},
        ),
    )
    assert.Equal(t,
        &ListNode{7, &ListNode{0, &ListNode{0, &ListNode{1, nil}}}},
        addTwoNumbers(
            &ListNode{2, &ListNode{4, &ListNode{5, nil}}},
            &ListNode{5, &ListNode{6, &ListNode{4, nil}}},
        ),
    )
    assert.Equal(t,
        &ListNode{7, &ListNode{0, &ListNode{8, &ListNode{1, nil}}}},
        addTwoNumbers(
            &ListNode{2, &ListNode{4, &ListNode{3, &ListNode{1, nil}}}},
            &ListNode{5, &ListNode{6, &ListNode{4, nil}}},
        ),
    )
    assert.Equal(t,
        &ListNode{7, &ListNode{0, &ListNode{8, &ListNode{1, nil}}}},
        addTwoNumbers(
            &ListNode{2, &ListNode{4, &ListNode{3, nil}}},
            &ListNode{5, &ListNode{6, &ListNode{4, &ListNode{1, nil}}}},
        ),
    )
}

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
