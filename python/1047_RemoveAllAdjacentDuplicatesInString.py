class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if len(stack) > 0 and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)

        return "".join(stack)
