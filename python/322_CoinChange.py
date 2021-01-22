import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [math.inf] * (amount + 1)
        for v in range(len(dp)):
            for coin in coins:
                if v < coin:
                    continue
                if v == coin:
                    dp[v] = 1
                    break
                dp[v] = min(dp[v], dp[v - coin] + 1)
        return dp[amount] if dp[amount] != math.inf else -1
