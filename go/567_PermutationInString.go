package main

func checkInclusion(s1 string, s2 string) bool {
    h := make([]int, 26)
    // 把 s1 每个字符的数量存在数组中
    for _, v := range s1 {
        h[v-'a'] ++
    }
    for i, v := range s2 {
        c := v - 'a'
        h[c] --
        if i >= len(s1) {
            h[s2[i-len(s1)]-'a'] ++
        }
        if isAllZero(h) {
            return true
        }
    }
    return false
}

func isAllZero(h []int) bool {
    for _, v := range h {
        if v != 0 {
            return false
        }
    }
    return true
}
