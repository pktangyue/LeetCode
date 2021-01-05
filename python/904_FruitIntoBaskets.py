from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # 只包含当前2种水果的起点
        start = 0
        # one 和 two 记录2种水果最后出现的(位置，种类)
        one = None
        two = None
        # 结果
        ret = 0
        for i in range(len(tree)):
            if not one or one[1] == tree[i]:
                one = (i, tree[i])
            elif not two or two[1] == tree[i]:
                two = (i, tree[i])
            else:
                # 出现第三种水果时
                # start 需要更新为较先出现的一种水果的位置 + 1
                # one 更新为保留的一种水果最后出现的位置
                # two 更新为当前出现的第三种水果的位置
                start, one, two = min(one, two)[0] + 1, max(one, two), (i, tree[i])
            ret = max(ret, i - start + 1)

        return ret
