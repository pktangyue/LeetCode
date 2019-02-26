from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 本质就是使分配在某个点左右两边的数量相等或差值为1
        nums.sort()
        target = nums[len(nums) // 2]
        return sum(abs(target - v) for v in nums)
