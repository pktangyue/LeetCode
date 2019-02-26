package main

import "sort"

func minMoves2(nums []int) int {
    // 本质就是使分配在某个点左右两边的数量相等或差值为1
    sort.Ints(nums)
    target := nums[len(nums)/2]
    moves := 0
    for _, v := range nums {
        if v > target {
            moves += v - target
        } else {
            moves += target - v
        }
    }
    return moves
}
