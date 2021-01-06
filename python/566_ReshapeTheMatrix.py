from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r0, c0 = len(nums), len(nums[0])
        if r0 * c0 != r * c:
            return nums
        ret = [[0] * c for _ in range(r)]
        for i in range(r * c):
            ret[i // c][i % c] = nums[i // c0][i % c0]
        return ret
