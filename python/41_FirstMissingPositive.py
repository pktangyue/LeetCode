from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 对于 len(nums) 完整的序列是 [1,n]
        # 这里添加一个0，使序列变为 [0,n] 方便 hash
        nums.append(0)
        l = len(nums)
        # 先排除 < 0 的数字 和 >= l 的
        for i in range(l):
            if nums[i] < 0 or nums[i] >= l:
                nums[i] = 0

        # 遍历使 nums[i] = num[i] + (count * l)， count 表示 i 在数组中出现的次数
        for v in nums:
            nums[v % l] += l

        for i in range(1, l):
            # 根据上面的公式，可以计算出 i 出现的次数。第一个为0的就是我们要找的
            count = nums[i] // l
            if count == 0:
                return i

        return l
