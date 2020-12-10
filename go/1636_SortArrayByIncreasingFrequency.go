package main

import "sort"

func frequencySort(nums []int) []int {
	type A struct {
		num  int
		freq int
	}
	m := make(map[int]int, len(nums))
	for _, num := range nums {
		m[num]++
	}
	s := make([]A, 0, len(m))
	for k, v := range m {
		s = append(s, A{k, v})
	}
	sort.Slice(s, func(i, j int) bool {
		if s[i].freq != s[j].freq {
			return s[i].freq < s[j].freq
		}
		return s[i].num > s[j].num
	})
	ret := make([]int, 0, len(nums))
	for _, v := range s {
		for i := 0; i < v.freq; i++ {
			ret = append(ret, v.num)
		}
	}
	return ret
}
