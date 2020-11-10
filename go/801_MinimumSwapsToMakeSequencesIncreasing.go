package main

func minSwap(A []int, B []int) int {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	swap, fix := 1, 0
	for i := 1; i < len(A); i++ {
		if (A[i-1] >= B[i] || B[i-1] >= A[i]) {
			// i-1 不动的情况下，i也不用动
			// i-1 交换了的情况下，i也得交换
			// fix = fix;
			swap++;
		} else if (A[i-1] >= A[i] || B[i-1] >= B[i]) {
			// i-1交换了，则i不交换
			// i-1没交换，这i需要交换
			fix, swap = swap, fix+1
		} else {
			// 这种情况下，不用动，取最小值
			t := min(swap, fix)
			swap = t + 1
			fix = t
		}
	}
	return min(swap, fix)
}
