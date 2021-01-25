from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        # 排除最小的1/3的数据，然后取偶数位的总和
        return sum(v for i, v in enumerate(piles[0:2 * len(piles) // 3]) if i % 2 == 1)
