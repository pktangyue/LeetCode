package main

func lengthOfLongestSubstring(s string) int {
    var start, max, new_index int
    h := make([]int, 128)
    for index, v := range s {
        // new_index 设为 index + 1 避免和 h 的初始化数据冲突
        new_index = index + 1
        // 当前 v 对应的index大于 start，则start需要更新
        if h[v] >= start {
            start = h[v]
        }
        // 检查是否有需要更新 max
        if new_index-start > max {
            max = new_index - start
        }
        // 更新 v 对应的 index
        h[v] = new_index
    }
    return max
}
