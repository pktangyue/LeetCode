class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        reverse_s = s[::-1]
        # dp[i][j] 表示 s[0:i] 和 reverse_s[0:j] 共有子序列（可分散，不连续）的最大长度
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == reverse_s[j] else max(dp[i][j + 1], dp[i + 1][j])
        return n - dp[n][n]
