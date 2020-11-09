package main

func carPooling(trips [][]int, capacity int) bool {
	s := make([]int, 1000)
	// 遍历每条路线，叠加每个点需要的容量
	for _, trip := range trips {
		for i := trip[1]; i < trip[2]; i++ {
			s[i] += trip[0]
		}
	}
	// 看看是否有超过容量的
	for _, v := range s {
		if v > capacity {
			return false
		}
	}
	return true
}
