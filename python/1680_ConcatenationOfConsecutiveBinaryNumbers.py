class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans, l, MOD = 0, 0, 10 ** 9 + 7
        for x in range(1, n + 1):
            if x & (-x) == x:
                l += 1
            ans = (ans * (1 << l) + x) % MOD
        return ans
