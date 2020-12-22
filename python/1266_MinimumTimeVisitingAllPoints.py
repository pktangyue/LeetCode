from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ret = 0
        for i in range(1, len(points)):
            l = abs(points[i][0] - points[i - 1][0])
            h = abs(points[i][1] - points[i - 1][1])
            ret += min(l, h) + abs(l - h)

        return ret
