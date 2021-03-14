from typing import List


# !!! 超时
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        nodes = {}

        # 构建图
        def addNode(v1, v2):
            if v1 in nodes:
                nodes[v1].append(v2)
            else:
                nodes[v1] = [v2]

        for v in pairs:
            addNode(v[0], v[1])
            addNode(v[1], v[0])
        # 找出有几张独立的图
        visited = [False] * len(s)

        def dfs(i):
            if visited[i]:
                return None
            if i not in nodes:
                return None
            visited[i] = True
            ret = {i}
            for v in nodes[i]:
                tmp = dfs(v)
                if tmp:
                    ret |= tmp
            return ret

        ret = list(s)
        for i in range(len(s)):
            g = dfs(i)
            if g:
                g = list(g)
                substr = []
                for v in g:
                    substr.append(s[v])
                substr.sort()
                for i in range(len(g)):
                    ret[g[i]] = substr[i]

        return "".join(ret)
