package main

func minDeletionSize(A []string) int {
	maxfunc := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	dp := make([]int, len(A[0]))
	for i := 0; i < len(dp); i++ {
		dp[i] = 1
	}
	// dp[i] 的含义为，在[i,)范围内，必须保留i位置的字母时，最多能保留多少个字母
	for i := len(dp) - 2; i >= 0; i-- {
		for j := i + 1; j < len(dp); j++ {
			valid := true
			for _, s := range A {
				if s[i] > s[j] {
					valid = false
					break
				}
			}
			if valid {
				// 在保留i的前提下，允许保留j时，更新状态
				dp[i] = maxfunc(dp[i], 1+dp[j])
			}
		}
	}
	m := 0
	for _, v := range dp {
		m = maxfunc(m, v)
	}
	return len(dp) - m
}
