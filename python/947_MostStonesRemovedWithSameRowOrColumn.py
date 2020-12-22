from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        l = len(stones)
        graph = defaultdict(set)
        for i in range(l):
            for j in range(i + 1, l):
                a = stones[i]
                b = stones[j]
                if a[0] == b[0] or a[1] == b[1]:
                    graph[i].add(j)
                    graph[j].add(i)

        visited = [False] * l
        ret = 0
        for i in range(l):
            if visited[i]:
                continue
            # 找到从i开始，找到能经过的所有点，形成一条路径
            stack = [i]
            visited[i] = True
            while stack:
                ret += 1
                node = stack.pop()
                for v in graph[node]:
                    if not visited[v]:
                        stack.append(v)
                        visited[v] = True

            # 每条路径需要保留1个
            ret -= 1

        return ret
