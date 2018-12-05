package main

func checkDuplicateWin(s string, win_ele byte) (bool, byte) {
    if s == "XXX" {
        if win_ele == 'O' {
            return false, 0
        }
        win_ele = 'X'
    } else if s == "OOO" {
        if win_ele == 'X' {
            return false, 0
        }
        win_ele = 'O'
    }
    return true, win_ele
}

func validTicTacToe(board []string) bool {
    // 记录是否已有连成线的
    var win_ele byte
    var valid bool
    var x_count, o_count int
    // 遍历竖排，并分别计算 X O 的个数
    for j := 0; j < 3; j++ {
        eles := make([]byte, 3)
        for i := 0; i < 3; i ++ {
            eles[i] = board[i][j]
            if board[i][j] == 'X' {
                x_count ++
            } else if board[i][j] == 'O' {
                o_count ++
            }
        }
        valid, win_ele = checkDuplicateWin(string(eles), win_ele)
        if ! valid {
            return false
        }
    }
    // 检查个数
    if ! (x_count == o_count || x_count-1 == o_count) {
        return false
    }
    // 遍历横排
    for i := 0; i < 3; i ++ {
        valid, win_ele = checkDuplicateWin(board[i], win_ele)
        if ! valid {
            return false
        }
    }
    // 遍历2个对角线
    valid, win_ele = checkDuplicateWin(string([]byte{board[0][0], board[1][1], board[2][2]}), win_ele)
    if ! valid {
        return false
    }
    valid, win_ele = checkDuplicateWin(string([]byte{board[0][2], board[1][1], board[2][0]}), win_ele)
    if ! valid {
        return false
    }
    // 检查连成线情况下的 X O 个数
    if win_ele == 'O' {
        return x_count == o_count
    } else if win_ele == 'X' {
        return x_count-1 == o_count
    } else {
        return true
    }
}
