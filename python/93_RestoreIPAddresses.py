from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        for numbers in self.getValidNumbers(4, s):
            ret.append(".".join(numbers))
        return ret

    def getValidNumbers(self, n: int, s: str) -> List[List[str]]:
        ret = []
        if len(s) == 0 or (len(s) > n * 3 and n != 1):
            return ret

        if n == 1 and self.isValidNumber(s):
            ret.append([s])
            return ret

        for i in range(len(s)):
            if not self.isValidNumber(s[:i + 1]):
                return ret
            for numbers in self.getValidNumbers(n - 1, s[i + 1:]):
                ret.append([s[:i + 1]] + numbers)

        return ret

    def isValidNumber(self, s: str) -> bool:
        num = int(s)
        if s[0] == '0' and len(s) > 1:
            return False
        if num > 255:
            return False
        return True
