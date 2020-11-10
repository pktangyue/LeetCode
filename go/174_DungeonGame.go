package main

func calculateMinimumHP(dungeon [][]int) int {
	maxfunc := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	minfunc := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	m, n := len(dungeon), len(dungeon[0])
	minHP := make([][]int, m)
	for i := m - 1; i >= 0; i-- {
		minHP[i] = make([]int, n)
		for j := n - 1; j >= 0; j-- {
			if i == m-1 && j == n-1 {
				minHP[i][j] = maxfunc(1, 1-dungeon[i][j])
			} else if i == m-1 {
				minHP[i][j] = maxfunc(1, minHP[i][j+1]-dungeon[i][j])
			} else if j == n-1 {
				minHP[i][j] = maxfunc(1, minHP[i+1][j]-dungeon[i][j])
			} else {
				minHP[i][j] = maxfunc(1, minfunc(minHP[i+1][j], minHP[i][j+1])-dungeon[i][j])
			}
		}
	}
	return minHP[0][0]
}
