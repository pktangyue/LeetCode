package main

func minKBitFlips(A []int, K int) int {
	ret := 0
	// 当前用于判断的flag
	flag := 1
	// 记录需要翻转flag的位置
	dp := make([]int, len(A)+1)
	for i := 0; i < len(A); i++ {
		// 回翻flag
		flag ^= dp[i]
		if flag == A[i] {
			continue
		}
		if i+K > len(A) {
			return -1
		}
		ret++
		// 翻转flag
		flag ^= 1
		// 记录回翻flag的位置
		dp[i+K] ^= 1
	}
	return ret
}
