package main

import (
    "strings"
)

func restoreIpAddresses(s string) []string {
    var ret []string
    for _, v := range getValidNumbers(4, s) {
        ret = append(ret, strings.Join(v, "."))
    }
    return ret
}

func getValidNumbers(n int, s string) [][]string {
    ret := [][]string{}
    if len(s) == 0 || (len(s) > n*3 && n != 1) {
        return ret
    }
    if n == 1 && isValidNumbers(s) {
        return [][]string{{s}}
    }
    for i := range s {
        if !isValidNumbers(s[:i+1]) {
            return ret
        }
        for _, r := range getValidNumbers(n-1, s[i+1:]) {
            ret = append(ret, append([]string{s[:i+1]}, r...))
        }
    }
    return ret
}

func isValidNumbers(s string) bool {
    num := 0
    for _, v := range s {
        d := int(v - '0')
        num = num*10 + d
    }
    if s[0] == '0' && len(s) > 1 {
        return false
    }
    if num > 255 {
        return false
    }
    return true
}
