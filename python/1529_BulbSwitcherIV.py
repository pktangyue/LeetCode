class Solution:
    def minFlips(self, target: str) -> int:
        ret = 0
        cur = 0
        for v in target:
            if int(v) != cur:
                cur ^= 1
                ret += 1

        return ret
