package main

import "math"

func jump(nums []int) int {
	cache := make(map[int]int)
	var wrap func(nums []int) int
	wrap = func(nums []int) (ret int) {
		if v, ok := cache[len(nums)]; ok {
			return v
		}
		defer func() {
			cache[len(nums)] = ret
		}()
		if len(nums) <= 1 {
			return 0
		}
		if nums[0] == 0 {
			return math.MaxInt32
		}
		minSteps := math.MaxInt32
		for i := nums[0]; i > 0; i-- {
			if i >= len(nums) {
				continue
			}
			if steps := wrap(nums[i:]); steps <= 1 {
				// 倒序找，找到<=1就不需要继续了，已经是最小可能
				minSteps = steps
				break
			} else if steps < minSteps {
				minSteps = steps
			}
		}
		return 1 + minSteps
	}
	return wrap(nums)
}
