from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = 0
        for i in range(len(arr))[::-1]:
            if arr[i] > greatest:
                greatest, arr[i] = arr[i], greatest
            else:
                arr[i] = greatest

        arr[len(arr) - 1] = -1
        return arr
