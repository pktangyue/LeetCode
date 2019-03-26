from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = left_top = right_top = ret = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                left_top = max(left_top, height[left])
                ret += left_top - height[left]
                left += 1
            else:
                right_top = max(right_top, height[right])
                ret += right_top - height[right]
                right -= 1
        return ret
