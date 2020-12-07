package main

func findMinFibonacciNumbers(k int) int {
	cache := []int{0, 1, 1}
	for i := 3; true; i++ {
		n := cache[i-2] + cache[i-1]
		// k 是 fibonacci 中的一个值，直接返回1
		if n == k {
			return 1
		}
		// 找到最接近k的值
		if n > k {
			break
		}
		cache = append(cache, n)
	}
	ret := 0
	// 贪婪算法获取需要个数
	for i := len(cache) - 1; i >= 0; i-- {
		if k == 0 {
			break
		}
		if k < cache[i] {
			continue
		}
		ret++
		k -= cache[i]
	}
	return ret
}
