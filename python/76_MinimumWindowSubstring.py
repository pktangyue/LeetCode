import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t 还有多少当前没有被包含
        remain = len(t)
        # t 转化为字典
        m = {}
        for v in t:
            if v in m:
                m[v] += 1
            else:
                m[v] = 1

        ret = (-math.inf, math.inf)
        l = 0
        for r in range(len(s)):
            if s[r] not in m:
                continue
            # 更新当前剩余状态
            if m[s[r]] > 0:
                remain -= 1
            m[s[r]] -= 1
            # 已经满足条件，移动左侧边界，找到最小长度
            while remain == 0:
                if r - l < ret[1] - ret[0]:
                    ret = (l, r)
                if l >= len(s) - 1:
                    break
                if s[l] in m:
                    # 更新当前剩余状态
                    if m[s[l]] >= 0:
                        remain += 1
                    m[s[l]] += 1
                l += 1

        return s[ret[0]:ret[1] + 1] if ret[1] != math.inf else ""
