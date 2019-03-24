package main

func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
        return ""
    }
    var ret string
    for i := 0; i <= len(strs[0]); i++ {
        var c string
        for index, v := range strs {
            if i >= len(v) {
                return ret
            }
            if index == 0 {
                c = string(v[i])
            } else if c != string(v[i]) {
                return ret
            }
        }
        ret += c
    }
    return ret
}
