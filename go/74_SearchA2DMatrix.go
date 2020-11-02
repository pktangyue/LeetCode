package main

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 {
		return false
	}
	index := len(matrix) - 1
	for index >= 0 {
		if len(matrix[index]) == 0 {
			return false
		}
		first := matrix[index][0]
		if target == first {
			return true
		}
		if target < first {
			index--
			continue
		}
		for _, v := range matrix[index] {
			if v == target {
				return true
			}
		}
		// 目标行没找到则退出循环
		break
	}
	return false
}
