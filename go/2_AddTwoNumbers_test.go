package main

import (
    "github.com/stretchr/testify/assert"
    "testing"
)

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
