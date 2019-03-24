package main

import "sort"

func threeSum(nums []int) [][]int {
    ret := [][]int{}
    sort.Ints(nums)
    for left := 0; left < len(nums)-2; left++ {
        mid := left + 1
        right := len(nums) - 1
        if left > 0 && nums[left] == nums[left-1] {
            continue
        }
        for mid < right {
            total := nums[left] + nums[mid] + nums[right]
            if total == 0 {
                ret = append(ret, []int{nums[left], nums[mid], nums[right]})
                for mid < right && nums[mid] == nums[mid+1] {
                    mid++
                }
                for mid < right && nums[right] == nums[right-1] {
                    right--
                }
                mid++
                right--
            } else if total > 0 {
                right--
            } else {
                mid++
            }
        }
    }
    return ret
}
