class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ret = 0
        # sliding window
        i = 0
        cost = 0
        for j in range(len(s)):
            cost += abs(ord(s[j]) - ord(t[j]))
            if cost <= maxCost:
                ret = max(ret, j - i + 1)
            while cost > maxCost:
                cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
                if i >= j:
                    break
        return ret
