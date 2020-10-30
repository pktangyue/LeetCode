package main

func brokenCalc(X int, Y int) int {
	// X 只能-和* ，那反过来就是Y 只能+和/
	n := 0
	for Y > X {
		if Y%2 == 1 {
			Y++
			n++
		} else {
			Y /= 2
			n++
		}
	}
	return n + X - Y
}
