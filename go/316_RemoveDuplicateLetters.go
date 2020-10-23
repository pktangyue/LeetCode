package main

import "strings"

func removeDuplicateLetters(s string) string {
	if len(s) == 0 {
		return ""
	}
	m := make(map[uint8]int)
	for i := 0; i < len(s); i++ {
		m[s[i]] ++
	}
	pos := 0
	for i := 0; i < len(s); i++ {
		if s[i] < s[pos] {
			pos = i
		}
		m[s[i]] --
		if m[s[i]] == 0 {
			break
		}
	}
	return string([]byte{s[pos]}) + removeDuplicateLetters(strings.ReplaceAll(s[pos+1:], string([]byte{s[pos]}), ""))
}
