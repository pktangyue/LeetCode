from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.dp = [[self.m * self.n] * self.n for _ in range(self.m)]
        self.dp[0][0] = 0
        self.q = [(0, 0)]
        while self.q:
            self.bfs(*self.q.pop(0))

        return self.dp[self.m - 1][self.n - 1]

    def bfs(self, i: int, j: int):
        if not (0 <= i < self.m and 0 <= j < self.n):
            return
        if self.grid[i][j] > 10:
            return

        # 把 grid 中的值加 10 表示已经访问过了，节省额外储存空间
        self.grid[i][j] += 10
        cost = self.dp[i][j]
        value = self.grid[i][j]
        # 从当前点出发，可达的点和当前点cost一致，其他3个方向 cost 加 1
        if value % 10 == 1:
            self.setCost(i, j + 1, cost, False)
            self.setCost(i, j - 1, cost + 1, True)
            self.setCost(i + 1, j, cost + 1, True)
            self.setCost(i - 1, j, cost + 1, True)
            self.bfs(i, j + 1)
        elif value % 10 == 2:
            self.setCost(i, j + 1, cost + 1, True)
            self.setCost(i, j - 1, cost, False)
            self.setCost(i + 1, j, cost + 1, True)
            self.setCost(i - 1, j, cost + 1, True)
            self.bfs(i, j - 1)
        elif value % 10 == 3:
            self.setCost(i, j + 1, cost + 1, True)
            self.setCost(i, j - 1, cost + 1, True)
            self.setCost(i + 1, j, cost, False)
            self.setCost(i - 1, j, cost + 1, True)
            self.bfs(i + 1, j)
        elif value % 10 == 4:
            self.setCost(i, j + 1, cost + 1, True)
            self.setCost(i, j - 1, cost + 1, True)
            self.setCost(i + 1, j, cost + 1, True)
            self.setCost(i - 1, j, cost, False)
            self.bfs(i - 1, j)

    def setCost(self, i: int, j: int, cost: int, add: bool):
        if not (0 <= i < self.m and 0 <= j < self.n):
            return
        self.dp[i][j] = min(self.dp[i][j], cost)
        if add and self.grid[i][j] < 10:
            self.q.append((i, j))
