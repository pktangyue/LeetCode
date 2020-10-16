package main

func isPalindrome(x int) bool {
	if x == 0 {
		return true
	}
	if x < 0 || x%10 == 0 {
		return false
	}
	rev := 0
	// x 为 12321 时，最终 x = 12, rev = 123
	// x 为 1221 时，最终 x = 12, rev = 12
	for x > rev {
		rev = rev*10 + x%10
		x /= 10
	}
	return x == rev || x == rev/10
}
