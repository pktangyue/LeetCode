from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count = 0
        # 保证位置 0 为当前值，win_count 记录位置0的元素获胜了几次
        # 如果最后只剩下一个元素，则这个元素即数组中的最大值，无论k为多少，肯定是这个值获胜
        while len(arr) > 1:
            if arr[0] < arr[1]:
                win_count = 0
                arr.pop(0)
            else:
                arr.pop(1)
            win_count += 1
            if win_count >= k:
                break

        return arr[0]
