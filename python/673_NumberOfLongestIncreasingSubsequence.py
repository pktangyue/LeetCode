from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp[i] = (w,c) 记录包含第i个元素的情况下，拥有最长子序列(w)的个数(c)
        # 初始化为长度为1，个数为1，即只有自己
        dp = [(1, 1)] * len(nums)
        for i in range(len(nums)):
            for j in range(i)[::-1]:
                if nums[i] > nums[j]:
                    # 找到一个有效的j元素时，最长子序列在j的基础上加上1（即自己），然后更新个数
                    l = dp[j][0] + 1
                    if dp[i][0] < l:
                        dp[i] = (l, dp[j][1])
                    elif dp[i][0] == l:
                        dp[i] = (l, dp[i][1] + dp[j][1])

        # 找出最长子序列的长度，然后统计个数
        max_w = max(dp)[0]
        return sum(c for w, c in dp if w == max_w)
