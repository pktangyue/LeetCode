package main

func isBipartite(graph [][]int) bool {
	A := make(map[int]bool)
	B := make(map[int]bool)
	stack := make([]int, 0, len(graph))
	for len(stack) > 0 || len(A)+len(B) < len(graph) {
		// 找到一个起点
		if len(stack) == 0 {
			for node := range graph {
				if !A[node] && !B[node] {
					stack = append(stack, node)
					break
				}
			}
			continue
		}
		var node int
		node, stack = stack[0], stack[1:]
		// 把 node 加入 A/B， 把他的边加入 B/A
		// 如果发现在另一个集合已经存在，则直接返回 false
		// 把新加入到 A 和 B 的 node 添加到 stack 中，用户下一次遍历
		if B[node] {
			for _, anotherNode := range graph[node] {
				if B[anotherNode] {
					return false
				} else if !A[anotherNode] {
					A[anotherNode] = true
					stack = append(stack, anotherNode)
				}
			}
		} else {
			A[node] = true
			for _, anotherNode := range graph[node] {
				if A[anotherNode] {
					return false
				} else if !B[anotherNode] {
					B[anotherNode] = true
					stack = append(stack, anotherNode)
				}
			}
		}
	}
	return true
}

// 把 node 加入的 set，他所有边的另一个节点加入到 anotherSet
// 如果任何一个 node 出现在对方 set 里，则失败
func addAndCheck(node int, edges []int, set, anotherSet map[int]bool) bool {
	if anotherSet[node] {
		return false
	}
	set[node] = true
	for _, v := range edges {
		if set[v] {
			return false
		}
		anotherSet[v] = true
	}
	return true
}
