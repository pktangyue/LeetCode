class Solution:
    def checkDuplicateWin(self, s, win_ele):
        if s == "XXX":
            if win_ele == 'O':
                return False, 0
            win_ele = 'X'
        elif s == "OOO":
            if win_ele == 'X':
                return False, 0
            win_ele = 'O'
        return True, win_ele

    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        # 记录是否已有连成线的
        win_ele = ''
        # 检查 X O 个数
        o_count = sum(v.count('O') for v in board)
        x_count = sum(v.count('X') for v in board)
        if x_count != o_count and x_count - 1 != o_count:
            return False
        # 遍历横排
        for i in range(3):
            valid, win_ele = self.checkDuplicateWin(board[i], win_ele)
            if not valid:
                return False

        # 遍历竖排
        for j in range(3):
            valid, win_ele = self.checkDuplicateWin(board[0][j] + board[1][j] + board[2][j], win_ele)
            if not valid:
                return False

        # 遍历2个对角线
        valid, win_ele = self.checkDuplicateWin(board[0][0] + board[1][1] + board[2][2], win_ele)
        if not valid:
            return False
        valid, win_ele = self.checkDuplicateWin(board[0][2] + board[1][1] + board[2][0], win_ele)
        if not valid:
            return False

        # 检查连成线情况下的 X O 个数
        if win_ele == 'O':
            return x_count == o_count
        elif win_ele == 'X':
            return x_count - 1 == o_count
        else:
            return True
