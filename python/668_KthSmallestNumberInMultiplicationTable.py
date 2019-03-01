class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n
        while left < right:
            count = 0
            mid = (left + right) // 2
            # 计算小于 mid 的数有多少
            for i in range(1, m + 1):
                if mid > n * i:
                    count += n
                else:
                    count += mid // i
            # 更新范围
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return right
