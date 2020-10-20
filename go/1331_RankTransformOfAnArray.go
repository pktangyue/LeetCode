package main

import "sort"

func arrayRankTransform(arr []int) []int {
	ret := make([]int, len(arr))
	copy(ret, arr)
	sort.Ints(arr)
	m := make(map[int]int, len(arr))
	rank := 1
	for _, v := range arr {
		if _, ok := m[v]; !ok {
			m[v] = rank
			rank++
		}
	}
	for i := 0; i < len(ret); i++ {
		ret[i] = m[ret[i]]
	}
	return ret
}
