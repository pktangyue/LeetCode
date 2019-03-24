class Solution:
    def simplifyPath(self, path: str) -> str:
        stacks = []
        for v in path.split("/"):
            if not v or v == ".":
                continue
            elif v == "..":
                if stacks:
                    stacks.pop(len(stacks) - 1)
            else:
                stacks.append(v)
        return "/" + "/".join(stacks)
