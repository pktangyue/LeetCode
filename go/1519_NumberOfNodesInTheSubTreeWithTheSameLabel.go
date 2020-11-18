package main

func countSubTrees(n int, edges [][]int, labels string) []int {
	ret := make([]int, n)
	graph := make(map[int][]int)
	addGraph := func(from, to int) {
		if _, ok := graph[from]; ok {
			graph[from] = append(graph[from], to)
		} else {
			graph[from] = []int{to}
		}
	}
	for _, edge := range edges {
		// 这里因为是无向图，所有两个方向都需要加
		addGraph(edge[0], edge[1])
		addGraph(edge[1], edge[0])
	}
	var dfs func(node int) map[byte]int
	dfs = func(node int) map[byte]int {
		// 当前节点包含自身，肯定有1
		ret[node] = 1
		m := map[byte]int{labels[node]: 1}
		if children, ok := graph[node]; ok {
			for _, child := range children {
				// 已经访问过的不再计算
				if ret[child] > 0 {
					continue
				}
				for key, value := range dfs(child) {
					m[key] += value
					if key == labels[node] {
						ret[node] += value
					}
				}
			}
		}
		return m
	}
	dfs(0)
	return ret
}
