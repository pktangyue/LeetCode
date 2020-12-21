from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp 表示[i,j]这段数值，一号选手可以选择的最大数字 减去 二号选手选择的最大数字
        dp = [[0 for _ in range(len(nums))]] * len(nums)
        for i in range(len(nums) - 1)[::-1]:
            # 只有i时，肯定是num[i]自身
            dp[i][i] = nums[i]
            for j in range(i + 1, len(nums)):
                # a 表示选择了i之后的值
                a = nums[i] - dp[i + 1][j]
                # b 表示选择了j之后的值
                b = nums[j] - dp[i][j - 1]
                # 取可能的最大值
                dp[i][j] = max(a, b)

        return dp[0][-1] >= 0
