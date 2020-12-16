from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = 0
        ret = []
        for v in A:
            num *= 2
            if v:
                num += 1
            ret.append(num % 5 == 0)

        return ret