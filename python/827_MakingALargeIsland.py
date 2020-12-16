from typing import List, Optional


class Island:
    def __init__(self):
        self.area = 0

    def inc(self):
        self.area += 1


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.ret = 0
        l = len(grid)
        gridMap: List[List[Optional[Island]]] = [[None] * l for _ in range(l)]

        def dfs(i: int, j: int, island: Island = None):
            # 越界终止
            if i < 0 or i >= l or j < 0 or j >= l:
                return
            # 非岛屿终止
            if grid[i][j] == 0:
                return
            # 已经遍历终止
            if gridMap[i][j]:
                return
            if not island:
                island = Island()
            island.inc()
            gridMap[i][j] = island
            # 记录最大的岛
            self.ret = max(self.ret, island.area)
            dfs(i - 1, j, island)
            dfs(i + 1, j, island)
            dfs(i, j - 1, island)
            dfs(i, j + 1, island)

        # 先把所有的岛找出来
        for i in range(l):
            for j in range(l):
                dfs(i, j)

        def findAndAddIsland(islands, i: int, j: int):
            if i < 0 or i >= l or j < 0 or j >= l:
                return
            island = gridMap[i][j]
            if island and island not in islands:
                islands.append(island)

        # 一个个尝试把0变1，找出最大值
        for i in range(l):
            for j in range(l):
                if grid[i][j] == 1:
                    continue
                area = 1
                islands: List[Island] = []
                findAndAddIsland(islands, i - 1, j)
                findAndAddIsland(islands, i + 1, j)
                findAndAddIsland(islands, i, j - 1)
                findAndAddIsland(islands, i, j + 1)
                area += sum([v.area for v in islands])
                self.ret = max(self.ret, area)

        return self.ret
