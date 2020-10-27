package main

func solveNQueens(n int) [][]string {
	emptyBoard := make([][]byte, n)
	for i := 0; i < n; i++ {
		emptyBoard[i] = make([]byte, n)
		for j := 0; j < n; j++ {
			emptyBoard[i][j] = '.'
		}
	}
	ret := make([][]string, 0)
	var dfs func(board [][]byte, row int)
	var validate func(board [][]byte, row, col int) bool
	dfs = func(board [][]byte, row int) {
		if row == len(board) {
			// 找到一个解, 添加到返回结果中
			ret = append(ret, make([]string, n))
			for i := 0; i < n; i++ {
				ret[len(ret)-1][i] = string(board[i])
			}
			// 找到解，回溯
			return
		}
		for col := 0; col < len(board); col++ {
			board[row][col] = 'Q'
			if validate(board, row, col) {
				dfs(board, row+1)
			}
			// 重置
			board[row][col] = '.'
		}
		// 找不到解，也回溯
		return
	}
	validate = func(board [][]byte, row int, col int) bool {
		for i := 0; i < row; i++ {
			for j := 0; j < len(board); j++ {
				// 同一排或者斜向2个方向也存在Q，则不合法
				if board[i][j] == 'Q' &&
					(col == j ||
						col-j == row-i ||
						j-col == row-i) {
					return false
				}
			}
		}
		return true
	}
	dfs(emptyBoard, 0)
	return ret
}
