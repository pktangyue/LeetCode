class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ret = 0
        stack = 0
        for v in S:
            if v == '(':
                stack += 1
            elif v == ')':
                if stack > 0:
                    stack -= 1
                else:
                    ret += 1
        return ret + stack
