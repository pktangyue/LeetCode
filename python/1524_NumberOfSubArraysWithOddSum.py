from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        l = len(arr)
        # dp[i] 表示以 arr[i] 为起点的子数组拥有的 (和为奇数的个数，和为偶数的个数）
        dp = [[0, 0] for _ in range(l)]
        for i in range(l)[::-1]:
            isOdd = arr[i] % 2
            dp[i][0] = isOdd
            dp[i][1] = isOdd ^ 1
            if i + 1 < l:
                # 当 arr[i] 为奇数，加上dp[i+1]记录的偶数子数组个数
                # 当 arr[i] 为偶数，加上dp[i+1]记录的奇数子数组个数
                dp[i][0] += dp[i + 1][isOdd]
                dp[i][0] %= MOD
                dp[i][1] += dp[i + 1][isOdd ^ 1]
                dp[i][1] %= MOD

        return sum(v[0] for v in dp) % MOD
