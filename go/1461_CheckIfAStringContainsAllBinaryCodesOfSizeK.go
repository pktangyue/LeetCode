package main

func hasAllCodes(s string, k int) bool {
	r := make([]bool, 1<<k)
	for i := 0; i <= len(s)-k; i++ {
		v := 0
		for j := 0; j < k; j++ {
			switch s[i+j] {
			case '0':
				v = 2 * v
			case '1':
				v = 2*v + 1
			}
		}
		if v < len(r) {
			r[v] = true
		}
	}
	for _, v := range r {
		if v == false {
			return false
		}
	}
	return true
}
