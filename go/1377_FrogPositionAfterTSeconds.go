package main

func frogPosition(n int, edges [][]int, t int, target int) float64 {
	visited := []int{}
	probability := map[int]float64{1: float64(1)}
	stack := []int{1}
	for i := 0; i < t; i++ {
		if len(stack) == 0 {
			// 所有节点已过滤，则跳出循环
			break
		}
		newStacks := make(map[int][]int)
		for _, edge := range edges {
			// 寻找从stack中任意一点为起点的边，找到后把终点加入到newStacks中
			if find(stack, edge[0]) >= 0 {
				if find(visited, edge[1]) >= 0 {
					continue
				}
				if _, ok := newStacks[edge[0]]; ok {
					newStacks[edge[0]] = append(newStacks[edge[0]], edge[1])
				} else {
					newStacks[edge[0]] = []int{edge[1]}
				}
			} else if find(stack, edge[1]) >= 0 {
				if find(visited, edge[0]) >= 0 {
					continue
				}
				if _, ok := newStacks[edge[1]]; ok {
					newStacks[edge[1]] = append(newStacks[edge[1]], edge[0])
				} else {
					newStacks[edge[1]] = []int{edge[0]}
				}
			}
		}
		visited = append(visited, stack...)
		stack = stack[0:0]
		// 更新到达某点的概率
		for from, s := range newStacks {
			stack = append(stack, s...)
			// 更新该秒能到达的节点的概率
			for _, value := range s {
				probability[value] = probability[from] * (float64(1) / float64(len(s)))
			}
			// 因为不可能停留在上一个节点，所以重置概率为0
			probability[from] = 0.0
		}
	}
	return probability[target]
}

func find(s []int, value int) int {
	for i, v := range s {
		if v == value {
			return i
		}
	}
	return -1
}
