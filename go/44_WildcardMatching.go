package main

func isMatch(s string, p string) bool {
	sIndex := 0
	pIndex := 0
	lastStarIndex := -1
	lastStarMatchSIndex := -1
	for sIndex < len(s) {
		if pIndex < len(p) && (s[sIndex] == p[pIndex] || p[pIndex] == '?') {
			sIndex++
			pIndex++
		} else if pIndex < len(p) && p[pIndex] == '*' {
			lastStarIndex = pIndex
			lastStarMatchSIndex = sIndex
			pIndex++
		} else if lastStarIndex != -1 {
			// 不满足上述2种情况，这从上一次出现*的位置重新开始匹配
			pIndex = lastStarIndex + 1
			sIndex = lastStarMatchSIndex + 1
			lastStarMatchSIndex++
		} else {
			return false
		}
	}
	// s 全部匹配成功之后，检查p剩余的是否都是*
	for pIndex < len(p) {
		if p[pIndex] != '*' {
			return false
		}
		pIndex++
	}
	return true
}
