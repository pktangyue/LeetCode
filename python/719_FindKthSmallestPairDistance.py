from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def check(m):
            count = 0
            left = 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > m:
                    left += 1
                # 这里不需要遍历所有的可能，只需要一个个数
                count += right - left
            return count >= k

        largest = nums[-1] - nums[0]
        small = 0
        while largest > small:
            mid = (largest + small) // 2
            if check(mid):
                largest = mid
            else:
                small = mid + 1

        return small
