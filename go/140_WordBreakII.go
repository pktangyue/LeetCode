package main

import (
	"fmt"
	"strings"
)

func wordBreak(s string, wordDict []string) []string {
	var wrap func(sub string) []string
	cache := make(map[string][]string)
	wrap = func(sub string) (ret []string) {
		ret = make([]string, 0)
		// 缓存
		if v, ok := cache[sub]; ok {
			return v
		}
		defer func() {
			cache[sub] = ret
		}()

		for _, v := range wordDict {
			if sub == v {
				ret = append(ret, v)
				// 这里可能只是一个解，之前写成return，漏了不少解
				continue
			}
			if strings.HasPrefix(sub, v) {
				for _, ss := range wrap(sub[len(v):]) {
					ret = append(ret, fmt.Sprintf("%s %s", v, ss))
				}
			}
		}
		return ret
	}
	return wrap(s)
}
