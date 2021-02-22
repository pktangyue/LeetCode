from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:
            if v == "+":
                v2 = stack.pop()
                stack[-1] += v2
            elif v == "-":
                v2 = stack.pop()
                stack[-1] -= v2
            elif v == "*":
                v2 = stack.pop()
                stack[-1] *= v2
            elif v == "/":
                v2 = stack.pop()
                stack[-1] = int(stack[-1] / v2)
            else:
                stack.append(int(v))

        return stack[0]
