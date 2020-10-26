package main

func findRedundantDirectedConnection(edges [][]int) []int {
	// 额外添加的一条边只会造成三种情况
	// 一种是一个节点出现两个父节点
	// 一种是出现环
	// 最后一种是前两种并存
	// 所以解决问题主要是找到这两种情况
	paths := make([][]int, 0)
	// 可能出现的环路
	circlePathIndex := -1
	// 组成环路的最后一条边
	var circleLastEdge []int
	// 可能出现2个父节点的第一条边
	var firstEdge []int
	firstEdgePathIndex := -1
	// 可能出现2个父节点的第二条边
	var secondEdge []int
	secondEdgePathIndex := -1
	for _, edge := range edges {
		addIndex := -1
		for i, path := range paths {
			if hasCircle(path) {
				continue
			}
			if success, newPath := addToPath(path, edge); success {
				paths[i] = newPath
				addIndex = i
				if hasCircle(newPath) {
					circlePathIndex = i
					circleLastEdge = edge
				}
				break
			}
		}
		if addIndex == -1 {
			paths = append(paths, edge)
			addIndex = len(paths) - 1
		}
		for i, path := range paths {
			if i == addIndex {
				continue
			}
			if conflictEdge := findConflictEdge(path, edge); conflictEdge != nil {
				firstEdge = conflictEdge
				firstEdgePathIndex = i
				secondEdge = edge
				secondEdgePathIndex = addIndex
				break
			}
		}
	}
	if circlePathIndex == -1 {
		return secondEdge
	}
	if firstEdgePathIndex == -1 || secondEdgePathIndex == -1 {
		return circleLastEdge
	}
	if circlePathIndex == firstEdgePathIndex {
		return firstEdge
	}
	if circlePathIndex == secondEdgePathIndex {
		return secondEdge
	}
	return nil
}

func findConflictEdge(path, edge []int) []int {
	for i, v := range path {
		if v == edge[1] && i > 0 {
			return []int{path[i-1], path[i]}
		}
	}
	return nil
}

func addToPath(path []int, edge []int) (bool, []int) {
	if path[len(path)-1] == edge[0] {
		return true, append(path, edge[1])
	}
	if path[0] == edge[1] {
		return true, append([]int{edge[0]}, path...)
	}
	return false, nil
}

func hasCircle(path []int) bool {
	m := make(map[int]bool, 0)
	for _, v := range path {
		if m[v] {
			return true
		}
		m[v] = true
	}
	return false
}
