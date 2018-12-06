class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 本质就是最大数-K和最小数+K的差值
        return max(0, (max(A) - K) - (min(A) + K))
