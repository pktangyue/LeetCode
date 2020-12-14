from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 10 ** 6
        ret = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                ret = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                ret.append([arr[i - 1], arr[i]])

        return ret
