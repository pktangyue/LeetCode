package main

func findKthNumber(m int, n int, k int) int {
    left, right := 1, m*n
    for left < right {
        count := 0
        mid := (left + right) / 2
        // 计算小于 mid 的数有多少
        for i := 1; i <= m; i++ {
            if mid > n*i {
                count += n
            } else {
                count += mid / i
            }
        }
        // 更新范围
        if count >= k {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return right
}
