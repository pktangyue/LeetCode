class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1, 2]
        if n > 2:
            for i in range(3, n + 1):
                num = 0
                # 已j作为root的情况
                for j in range(1, i + 1):
                    # 左节点个数
                    leftnum = dp[j - 1]
                    # 右节点个数
                    rightnum = dp[i - j]
                    # 左右分别是独立的情况，结果需要相乘
                    num += leftnum * rightnum
                dp.append(num)
        return dp[n]
