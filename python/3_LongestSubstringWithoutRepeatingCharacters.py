class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = start = 0
        h = {}
        for index, v in enumerate(s):
            # new_index 设为 index + 1 避免和 h 的初始化数据冲突
            new_index = index + 1
            # 当前 v 对应的index大于 start，则start需要更新
            if h.get(v, 0) >= start:
                start = h.get(v, 0)
            # 检查是否有需要更新 max
            if new_index - start > ret:
                ret = new_index - start
            # 更新 v 对应的 index
            h[v] = new_index
        return ret
