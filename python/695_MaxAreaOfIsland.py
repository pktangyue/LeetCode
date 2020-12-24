from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ret = 0

        def dfs(i: int, j: int) -> int:
            if not (0 <= i < len(grid) and 0 <= j < len(grid[i])):
                return 0
            if not grid[i][j]:
                return 0
            grid[i][j] = 0
            c = 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            self.ret = max(self.ret, c)
            return c

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dfs(i, j)

        return self.ret
