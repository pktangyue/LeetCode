package main

import "sort"

func deleteAndEarn(nums []int) int {
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	cache := make(map[int]int)
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	var wrap func(nums []int, start int) int
	wrap = func(nums []int, start int) (ret int) {
		// 缓存
		if v, ok := cache[start]; ok {
			return v
		}
		defer func() {
			cache[start] = ret
		}()
		// 找到从start开始，最大数字和最大数字-1的位置，最大数字-1的数量可能为0
		var first, second int
		lastFirstIndex, lastSecondIndex := -1, -1
		for i := start; i < len(nums); i++ {
			if first == 0 {
				first = nums[i]
				second = nums[i] - 1
				continue
			}
			if first == nums[i] {
				continue
			}
			if lastFirstIndex == -1 {
				lastFirstIndex = i
			}
			if second == nums[i] {
				continue
			}
			if lastSecondIndex == -1 {
				lastSecondIndex = i
			}
			break
		}
		// 只剩最大数字
		if lastFirstIndex == -1 {
			return (len(nums) - start) * first
		}
		// 只剩最大数字和最大数字-1
		if lastSecondIndex == -1 {
			return max((lastFirstIndex-start)*first, (len(nums)-lastFirstIndex)*second)
		}
		// 还有其他数字
		return max((lastFirstIndex-start)*first+wrap(nums, lastSecondIndex), wrap(nums, lastFirstIndex))
	}
	return wrap(nums, 0)
}
