package main

func numSubarraysWithSum(A []int, S int) int {
	left, count, ret := 0, 0, 0
	for i, v := range A {
		if v == 1 {
			count++
		}
		// 总数大于S时，需要更新left
		if count > S {
			for j := left; j <= i; j++ {
				if A[j] == 1 {
					count--
					if count == S {
						left = j + 1
						break
					}
				}
			}
		}
		// 得到目标数后，计算从左起，有多少0，就有多少个组合
		if count == S {
			for j := left; j <= i; j++ {
				ret++
				if A[j] == 1 {
					break
				}
			}
		}
	}
	return ret
}
