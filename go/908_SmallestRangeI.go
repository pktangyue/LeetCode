package main

func smallestRangeI(A []int, K int) int {
    // 本质就是最大数-K和最小数+K的差值
    min, max := 10000, 0
    for _, v := range A {
        if max < v {
            max = v
        }
        if min > v {
            min = v
        }
    }
    if min+K > max-K {
        return 0
    } else {
        return (max - K) - (min + K)
    }
}
