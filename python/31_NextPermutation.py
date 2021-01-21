from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        # 找到 index，使得 nums[index] > nums[index - 1]
        index = len(nums) - 1
        while True:
            if index == 0:
                break
            if nums[index] > nums[index - 1]:
                break
            index -= 1

        # 翻转 [index, len(nums))，使其变为最小
        for i in range(len(nums) - index):
            left = index + i
            right = len(nums) - i - 1
            if left >= right:
                break
            nums[left], nums[right] = nums[right], nums[left]

        # 翻转结束后，如果 index-1 存在，把它和大于它的最小数字交换, 使[index-1,l) 大约原始的值
        if index - 1 >= 0:
            for i in range(index, len(nums)):
                if nums[i] > nums[index - 1]:
                    nums[i], nums[index - 1] = nums[index - 1], nums[i]
                    break
