from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            h = defaultdict(int)
            for c in s:
                h[c] += 1

            sign = sum([(k, h[k]) for k in sorted(h.keys())], tuple())
            m[sign].append(s)

        return list(m.values())
