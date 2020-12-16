from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        l, r = 0, len(nums) - 1
        s1, s2 = nums[l], nums[r]
        # 分别从左，从右开始累加
        while l < r - 1:
            if s2 < s1:
                r -= 1
                s2 += nums[r]
            else:
                l += 1
                s1 += nums[l]

        # 如果左侧总和大于右侧，需要修正，让右侧多增加一个数字
        if s1 >= s2:
            r -= 1

        return nums[r:len(nums)][::-1]
