from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                ret[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return ret
