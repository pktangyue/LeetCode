package main

func strStr(haystack string, needle string) int {
	// https://www.inf.hs-flensburg.de/lang/algorithmen/pattern/kmpen.htm
	if len(needle) == 0 {
		return 0
	}
	b := make([]int, len(needle)+1)
	i, j := 0, -1
	b[0] = -1
	for i < len(needle) {
		for j >= 0 && needle[i] != needle[j] {
			j = b[j]
		}
		i++
		j++
		b[i] = j
	}
	i, j = 0, 0
	for i < len(haystack) {
		for j >= 0 && needle[j] != haystack[i] {
			j = b[j]
		}
		i++
		j++
		if j == len(needle) {
			return i - len(needle)
		}
	}
	return -1
}
