package main

import "sort"

func videoStitching(clips [][]int, T int) int {
	sort.Slice(clips, func(i, j int) bool {
		if clips[i][0] == clips[j][0] {
			return clips[i][1] < clips[j][1]
		}
		return clips[i][0] < clips[j][0]
	})
	n := -1
	left, right := 0, 0
	for _, v := range clips {
		if right >= T {
			break
		}
		// 找到第一个从0开始的
		if v[0] == 0 && n == -1 {
			n = 1
			right = v[1]
			continue
		}
		// 替换之前的一个clip
		if v[0] <= left && v[1] > right {
			right = v[1]
			continue
		}
		// 找到下一个连续的clip，更新left，right
		if v[0] > left && v[0] <= right && v[1] > right {
			left, right = right, v[1]
			n++
			continue
		}
	}
	if right < T {
		return -1
	}
	return n
}
