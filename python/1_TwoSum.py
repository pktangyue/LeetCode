class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, value in enumerate(nums):
            if value in h:
                return [h[value], i]
            else:
                h[target - value] = i
        return None
