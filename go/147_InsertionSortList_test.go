package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInsertionSortList(t *testing.T) {
	//assert.Equal(t,
	//	&ListNode{
	//		Val: 1,
	//		Next: &ListNode{
	//			Val: 2,
	//			Next: &ListNode{
	//				Val: 3,
	//				Next: &ListNode{
	//					Val:  4,
	//					Next: nil,
	//				},
	//			},
	//		},
	//	},
	//	insertionSortList(&ListNode{
	//		Val: 4,
	//		Next: &ListNode{
	//			Val: 2,
	//			Next: &ListNode{
	//				Val: 1,
	//				Next: &ListNode{
	//					Val:  3,
	//					Next: nil,
	//				},
	//			},
	//		},
	//	}),
	//)
	assert.Equal(t,
		&ListNode{
			Val: -1,
			Next: &ListNode{
				Val: 0,
				Next: &ListNode{
					Val: 3,
					Next: &ListNode{
						Val: 4,
						Next: &ListNode{
							Val:  5,
							Next: nil,
						},
					},
				},
			},
		},
		insertionSortList(&ListNode{
			Val: -1,
			Next: &ListNode{
				Val: 5,
				Next: &ListNode{
					Val: 3,
					Next: &ListNode{
						Val: 4,
						Next: &ListNode{
							Val:  0,
							Next: nil,
						},
					},
				},
			},
		}),
	)
}
