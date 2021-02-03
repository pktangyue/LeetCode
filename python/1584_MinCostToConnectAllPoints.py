import math
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        ret = 0
        visited = [0]
        cur = 0
        # 表示非 visited 里面的点 到 由 visited 中的点，其中最小距离的值
        dp = [math.inf] * len(points)
        while len(visited) < len(points):
            for i in range(len(points)):
                if i in visited:
                    continue
                cost = abs(points[i][0] - points[cur][0]) + abs(points[i][1] - points[cur][1])
                dp[i] = min(dp[i], cost)
            # 找到最短的边，以及对应的 index，并设置为下一次循环的 cur 值
            minCost, cur = min((v, i) for i, v in enumerate(dp))
            ret += minCost
            visited.append(cur)
            # 排除已经遍历的index，避免干扰寻找最短边
            dp[cur] = math.inf
        return ret
