package main

func numBusesToDestination(routes [][]int, S int, T int) int {
	if S == T {
		return 0
	}
	if len(routes) == 0 {
		return -1
	}
	reachable := map[int]int{S: 0}
	for true {
		updated := false
		leftRoutes := make([][]int, 0, len(routes))
		for _, route := range routes {
			// 获取到达该线路需要乘坐的最少bus数量
			if min := getMinOfRoute(reachable, route); min != -1 {
				for _, s := range route {
					// 更新到达某个站点的最短距离
					if n, ok := reachable[s]; (ok && n > min) || !ok {
						reachable[s] = min + 1
						updated = true
					}
				}
			} else {
				leftRoutes = append(leftRoutes, route)
			}
		}
		// 如果没有新的可到达站点，退出寻找
		if !updated {
			break
		}
		// 排除已更新路由表的路线
		routes = leftRoutes
	}
	// 最后在路由表中查找到达T站的最短距离
	if n, ok := reachable[T]; ok {
		return n
	} else {
		return -1
	}
}

func getMinOfRoute(reachable map[int]int, route []int) int {
	min := -1
	for _, s := range route {
		if n, ok := reachable[s]; ok {
			if min == -1 || min > n {
				min = n
			}
		}
	}
	return min
}
