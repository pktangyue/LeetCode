from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [0] * len(arr)

        def visit(i: int) -> int:
            # 如果已经访问过，直接返回
            if dp[i]:
                return dp[i]
            leftVisit = 0
            # 往左走，找出最大可访问数
            for j in range(max(0, i - d), i)[::-1]:
                if arr[j] >= arr[i]:
                    break
                leftVisit = max(leftVisit, visit(j))
            # 往右走，找出最大可访问数
            rightVisit = 0
            for j in range(i + 1, min(len(arr), i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                rightVisit = max(rightVisit, visit(j))
            # 左或右，选择最大的，加上自身，并保存状态
            dp[i] = 1 + max(leftVisit, rightVisit)
            return dp[i]

        for i in range(len(arr)):
            visit(i)

        return max(dp)
