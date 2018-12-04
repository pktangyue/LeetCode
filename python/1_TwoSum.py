class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(nums)):
            value = nums[i]
            if value in h:
                return [h[value], i]
            else:
                h[target - value] = i
        return None
