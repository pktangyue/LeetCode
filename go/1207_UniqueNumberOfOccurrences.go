package main

func uniqueOccurrences(arr []int) bool {
	count := make(map[int]int)
	for _, v := range arr {
		count[v]++
	}
	r := make(map[int]bool)
	for _, v := range count {
		if r[v] == true {
			return false
		}
		r[v] = true
	}
	return true
}
