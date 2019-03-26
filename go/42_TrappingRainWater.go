package main

func trap(height []int) int {
    if len(height) == 0 {
        return 0
    }
    var left, right, left_top, right_top, ret int
    right = len(height) - 1
    for left < right {
        if height[left] < height[right] {
            if height[left] > left_top {
                left_top = height[left]
            }
            ret += left_top - height[left]
            left++
        } else {
            if height[right] > right_top {
                right_top = height[right]
            }
            ret += right_top - height[right]
            right--
        }
    }
    return ret
}
