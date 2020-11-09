package main

func checkValidString(s string) bool {
	lo, hi := 0, 0
	for _, v := range s {
		if v == '(' {
			lo++
		} else {
			lo--
		}
		if v != ')' {
			hi++
		} else {
			hi--
		}
		if hi < 0 {
			break
		}
		if lo < 0 {
			lo = 0
		}
	}
	return lo == 0
}
