from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ss = [v for v in S.lower()]
        positions = {}
        char_count = 0
        for i, v in enumerate(ss):
            if v.isalpha():
                positions[char_count] = i
                char_count += 1

        ret = []
        for i in range(2 ** char_count):
            for j in range(char_count):
                if (i >> j) % 2 == 1:
                    ss[positions[j]] = ss[positions[j]].upper()
                else:
                    ss[positions[j]] = ss[positions[j]].lower()
            ret.append(''.join(ss))

        return ret
