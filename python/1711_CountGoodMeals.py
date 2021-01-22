from collections import defaultdict
from typing import List


class Solution:
    MOD = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        self.deliciousness = deliciousness
        self.ret = 0
        # deliciousness[i] 最大为 2**20，那么2个数之和最大就为 2**21
        for i in range(22):
            self.calc(2 ** i)
        return self.ret

    def calc(self, n):
        m = defaultdict(int)
        for v in self.deliciousness:
            self.ret += m[v]
            m[n - v] += 1
        self.ret %= self.MOD
