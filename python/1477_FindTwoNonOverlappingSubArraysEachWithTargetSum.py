import math
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ret = math.inf
        # dp[i] 表示截止到 i ，子数组和为 target 最小长度
        dp = [math.inf] * len(arr)
        t = 0
        i = j = 0
        # 滑动窗口，累计子数组和
        while j < len(arr):
            t += arr[j]
            while t > target:
                t -= arr[i]
                i += 1

            # j-1 的最小长度在 j 肯定也满足
            dp[j] = dp[j - 1] if j > 0 else math.inf
            if t == target:
                # 出现满足条件的情况，v 为子数组长度
                v = j - i + 1
                dp[j] = min(dp[j], v)
                # v + math.inf 仍为 math.inf
                ret = min(ret, v + (dp[i - 1] if i > 0 else math.inf))

            j += 1

        return ret if not math.isinf(ret) else -1
