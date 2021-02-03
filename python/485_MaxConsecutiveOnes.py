from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        cur = 0
        for i in range(len(nums) + 1):
            if i == len(nums) or nums[i] == 0:
                ret = max(ret, cur)
                cur = 0
                continue
            cur += 1

        return ret
