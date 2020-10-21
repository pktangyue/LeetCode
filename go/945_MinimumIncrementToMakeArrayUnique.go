package main

import (
	"sort"
)

func minIncrementForUnique(A []int) int {
	if len(A) == 0 {
		return 0
	}
	sort.Ints(A)
	ret := 0
	prev := -1
	// 排序后，从小到大依次加到比前一个数字大1就行了
	for i := 0; i < len(A); i++ {
		if A[i] > prev {
			prev = A[i]
			continue
		}
		diff := prev - A[i] + 1
		ret += diff
		prev = A[i] + diff
	}
	return ret
}
