from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return []
        ret = []
        for i in range(len(nums)):
            if len(ret) and nums[i] == ret[-1][1] + 1:
                ret[-1][1] = nums[i]
            else:
                ret.append([nums[i], nums[i]])

        return list(map(lambda x: "{}->{}".format(x[0], x[1]) if x[0] != x[1] else str(x[0]), ret))
