from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # 用于比较的目标
        target = k * threshold
        total = 0
        ret = 0
        for i in range(len(arr)):
            if i < k:
                total += arr[i]
                if i < k - 1:
                    continue
            else:
                total -= arr[i - k]
                total += arr[i]

            if total >= target:
                ret += 1

        return ret