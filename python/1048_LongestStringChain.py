from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        # dp = [(cnt, i)]，表示 i 位置最多包含个数，并记录位置 i
        dp = defaultdict(list)
        for i in range(len(words)):
            l = len(words[i])
            val = (1, i)
            for v in dp[l - 1]:
                if self.isPredecessor(words[v[1]], words[i]):
                    val = max(val, (v[0] + 1, i))
            dp[l].append(val)
        return max(sum(dp.values(), []))[0]

    def isPredecessor(self, a, b):
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(a) and (j == len(b) or j == len(b) - 1)
