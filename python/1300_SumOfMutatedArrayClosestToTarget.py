import math
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        min_diff = math.inf
        ret = math.inf
        total = 0
        for i, v in enumerate(arr):
            # 计算最接近 target-total 的平均数，如果大于当前 v，则取 v，这是因为只能减小数组中的值
            avg = min(v, round((target - total) / (len(arr) - i)))
            diff = abs(target - total - avg * (len(arr) - i))
            if abs(diff) < min_diff:
                min_diff = diff
                ret = avg
            elif abs(diff) == min_diff:
                ret = min(ret, avg)
            # 如果 ret 已经小于 v 了，则后续大于v的元素就没必要在计算了
            if v > ret:
                break
            total += v

        return ret
