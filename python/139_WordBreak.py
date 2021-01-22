from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 记录所有可能，使得s[position[i]:] 返回True
        positions = [len(s)]
        for i in range(len(s))[::-1]:
            for pos in positions:
                if s[i:pos] in wordDict:
                    positions.append(i)
                    break

        return 0 in positions
