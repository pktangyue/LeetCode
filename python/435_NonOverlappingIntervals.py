from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort()
        # dp[i] = [a,b,c] 表示包含 intervals[0:i] 的条件下，a 最大的前提下，[b,c] 最小
        dp = []
        for i in range(len(intervals)):
            val = [1, intervals[i][0], intervals[i][1]]
            for j in range(i)[::-1]:
                # 如果 dp[j][0] 小于 val[0]-1，则跳出循环，后续的肯定都无需计算
                if val[0] - 1 > dp[j][0]:
                    break
                if dp[j][2] <= intervals[i][0]:
                    # 可以合并的情况
                    tmp = [dp[j][0] + 1, dp[j][1], intervals[i][1]]
                else:
                    # 有交叉的情况
                    tmp = dp[j]
                # 取 a 较大的，c 较小的，b 较大的值
                val = max(tmp, val, key=lambda v: (v[0], -v[2], v[1]))
            dp.append(val)

        return len(intervals) - dp[-1][0]
