package main

import (
	"sort"
)

func minCost(n int, cuts []int) int {
	if len(cuts) == 0 {
		return 0
	}
	cuts = append(cuts, 0, n)
	sort.Ints(cuts)
	l := len(cuts)
	// dp[i][j] 表示i和j之间最少cost
	// i + 1 <= j 时为0
	dp := make([][]int, l)
	for i := 0; i < l; i++ {
		dp[i] = make([]int, l)
	}
	minfunc := func(x, y int) int {
		if x == 0 || y < x {
			return y
		}
		return x
	}
	// 自底向上
	for i := l - 2; i >= 0; i-- {
		for j := i + 2; j < l; j++ {
			min := 0
			for k := i + 1; k < j; k++ {
				min = minfunc(min, dp[i][k]+dp[k][j])
			}
			dp[i][j] = min + cuts[j] - cuts[i]
		}
	}
	return dp[0][l-1]
}
