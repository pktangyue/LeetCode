package main

func numSubarrayProductLessThanK(nums []int, k int) int {
	if k <= 1 {
		return 0
	}
	ret := 0
	left := 0
	v := 1
	for right := 0; right < len(nums); right++ {
		v *= nums[right]
		for v >= k {
			v /= nums[left]
			left++
		}
		ret += right - left + 1
	}
	return ret
}
