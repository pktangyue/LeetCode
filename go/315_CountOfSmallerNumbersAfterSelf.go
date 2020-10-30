package main

import (
	"math"
)

func countSmaller(nums []int) []int {
	ret := make([]int, len(nums))
	// m 可以优化为数组，减少for遍历
	m := make(map[int]int) // m 记录倒序遍历后，小于等于k的出现的次数
	for i := len(nums) - 1; i >= 0; i-- {
		largestK := math.MinInt32
		for k := range m {
			// 因为value包含等于k的数量，所有要找出小于k的数量
			if k > largestK && k < nums[i] {
				largestK = k
			}
			// 如果当前值小于k，则小于k的数量需要加1
			if nums[i] < k {
				m[k]++
			}
		}
		// 更新小于当前值的数量，之前没出现过在largestK的基础上加上本身
		// 出现过，直接加1（即本身）
		if m[nums[i]] == 0 {
			m[nums[i]] = 1 + m[largestK]
		} else {
			m[nums[i]]++
		}
		// 结果是largestK对应的数量
		ret[i] = m[largestK]
	}
	return ret
}
