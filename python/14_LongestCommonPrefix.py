from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ret = ""
        for i, s in enumerate(strs[0]):
            c = ""
            for j, v in enumerate(strs):
                if i >= len(v):
                    return ret
                if j == 0:
                    c = v[i]
                elif c != v[i]:
                    return ret
            ret += c
        return ret
