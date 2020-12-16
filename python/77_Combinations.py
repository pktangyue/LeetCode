from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return [list(v) for v in combinations(range(1, n + 1), k)]
        if k == 0:
            return [[]]
        # ret = []
        # for i in range(k, n + 1):
        #     for v in self.combine(i - 1, k - 1):
        #         ret.append(v + [i])
        # return ret
        return [v + [i] for i in range(k, n + 1) for v in self.combine(i - 1, k - 1)]
