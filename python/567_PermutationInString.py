class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h = [0] * 26
        # 把 s1 每个字符的数量存在数组中
        for v in s1:
            h[ord(v) - ord('a')] += 1
        for i, v in enumerate(s2):
            c = ord(v) - ord('a')
            h[c] -= 1
            if i >= len(s1):
                h[ord(s2[i - len(s1)]) - ord('a')] += 1
            if all(v == 0 for v in h):
                return True
        return False
