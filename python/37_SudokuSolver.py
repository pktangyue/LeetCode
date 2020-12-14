from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 小面板中包含的值
        subs = defaultdict(lambda: defaultdict(bool))
        # 列中包含的值
        cols = defaultdict(lambda: defaultdict(bool))
        # 行中包含的值
        rows = defaultdict(lambda: defaultdict(bool))
        # 初始化上面三个变量
        for i in range(9):
            for j in range(9):
                k = board[i][j]
                if k == ".":
                    continue
                subs[(i // 3, j // 3)][k] = True
                cols[j][k] = True
                rows[i][k] = True

        def backTracking(index: int) -> bool:
            # 遍历完成，找到解
            if index == 9 * 9:
                return True
            i = index // 9
            j = index % 9
            if board[i][j] != ".":
                # 默认有值，继续往下走
                return backTracking(index + 1)
            for v in range(9):
                # 转换为 1 到 9
                k = str(v + 1)
                # k 已经存在了，则跳过
                if subs[(i // 3, j // 3)][k] or cols[j][k] or rows[i][k]:
                    continue
                # 找到一个可能解
                board[i][j] = k
                subs[(i // 3, j // 3)][k] = True
                cols[j][k] = True
                rows[i][k] = True
                # 找到解这继续
                if backTracking(index + 1):
                    return True
                # 没找到解，回溯
                board[i][j] = "."
                subs[(i // 3, j // 3)][k] = False
                cols[j][k] = False
                rows[i][k] = False

            # 没找到解
            return False

        # 从(0,0)位置开始
        backTracking(0)
