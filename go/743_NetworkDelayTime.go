package main

import "math"

func networkDelayTime(times [][]int, N int, K int) int {
	graph := make(map[int][][]int)
	for _, v := range times {
		if _, ok := graph[v[0]]; ok {
			graph[v[0]] = append(graph[v[0]], []int{v[1], v[2]})
		} else {
			graph[v[0]] = [][]int{{v[1], v[2]}}
		}
	}
	visited := make([]int, N)
	timeMap := map[int]int{K: 0}
	for {
		// 找到距离最小，且没有访问过的点
		point := 0
		minTime := math.MaxInt32
		for i := 0; i < N; i++ {
			if visited[i] == 1 {
				continue
			}
			if time, ok := timeMap[i+1]; ok && time < minTime {
				minTime = time
				point = i + 1
			}
		}
		// 找不到最小的点，意味着遍历完毕
		if point == 0 {
			break
		}
		// 标记已遍历
		visited[point-1] = 1
		edges, ok := graph[point]
		if !ok {
			continue
		}
		// 更新可到达各点的最小距离
		for _, edge := range edges {
			newTime := timeMap[point] + edge[1]
			if time, ok := timeMap[edge[0]]; !ok || time > newTime {
				timeMap[edge[0]] = newTime
			}
		}
	}
	max := 0
	// 如果有任何一点不能到达，则返回-1
	for i := 1; i <= N; i++ {
		if v, ok := timeMap[i]; ok {
			if v > max {
				max = v
			}
		} else {
			return -1
		}
	}
	return max
}
