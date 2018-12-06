package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

func TestRemoveNthFromEnds(t *testing.T) {
    assert.Equal(t,
        &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{5, nil}}}},
        removeNthFromEnd(
            &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}},
            2,
        ),
    )
    assert.Equal(t,
        &ListNode{2, nil},
        removeNthFromEnd(
            &ListNode{1, &ListNode{2, nil}},
            2,
        ),
    )
    assert.Nil(t,
        removeNthFromEnd(
            &ListNode{1, nil},
            1,
        ),
    )
}
