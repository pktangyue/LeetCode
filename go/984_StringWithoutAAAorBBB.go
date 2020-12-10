package main

func strWithout3a3b(A int, B int) string {
	ret := ""
	change := false
	// 这里保证 A 大于 B，方便后面计算
	if B > A {
		A, B = B, A
		change = true
	}
	// 主要是一个比例问题，A 的范围肯定是 [B,2*(B+1)]
	for B > 0 {
		if A > B {
			A -= 2
			B -= 1
			if change {
				ret += "bb"
				ret += "a"
			} else {
				ret += "aa"
				ret += "b"
			}
		} else {
			A -= 1
			B -= 1
			if change {
				ret += "b"
				ret += "a"
			} else {
				ret += "a"
				ret += "b"
			}
		}
	}
	for A > 0 {
		A--
		if change {
			ret += "b"
		} else {
			ret += "a"
		}
	}
	return ret
}
