from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        # dp[i] 表示放完i本书后，需要的最小高度
        dp = [0] * len(books)
        for i in range(len(books)):
            width = books[i][0]
            height = books[i][1]
            # 第i本书先单独放一排
            dp[i] = dp[i - 1] + height if i > 0 else height
            # 尝试把之前的书合并到这一行，寻找更小的可能值
            for j in range(i)[::-1]:
                width += books[j][0]
                if width > shelf_width:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j - 1] + height if j > 0 else height)

        return dp[len(books) - 1]
