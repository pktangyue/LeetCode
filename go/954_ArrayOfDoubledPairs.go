package main

import "sort"

func canReorderDoubled(A []int) bool {
	sort.Ints(A)
	m := make(map[int]int)
	count := 0
	for _, v := range A {
		if v < 0 {
			if n, ok := m[v]; ok && n > 0 {
				m[v] --
				count--
			} else if v%2 == -1 {
				// 这里之前写成了 == 1，导致未通过
				// 作为最小的一个负数，切为奇数，则不可能匹配
				return false
			} else {
				m[v/2] ++
				count++
			}
		} else {
			if n, ok := m[v]; ok && n > 0 {
				m[v] --
				count--
			} else {
				m[v*2] ++
				count++
			}
		}
	}
	return count == 0
}
