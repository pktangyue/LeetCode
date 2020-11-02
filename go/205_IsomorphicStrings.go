package main

func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	m := make(map[byte]byte)
	for i := 0; i < len(s); i++ {
		from := s[i]
		if to, ok := m[from]; ok {
			if to != t[i] {
				return false
			}
		} else {
			m[from] = t[i]
		}
	}
	// 检查是否有相同的字母映射到了同一个字母
	r := make(map[byte]bool)
	for _, v := range m {
		if r[v] == true {
			return false
		}
		r[v] = true
	}
	return true
}
