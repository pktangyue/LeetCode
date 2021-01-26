class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        # 开头处的0和结尾处的1都不用考虑
        S = S.lstrip('0').rstrip('1')
        l = len(S)
        if l == 0:
            return 0
        ret = l
        # 包含 i 个字符时，包含几个1
        cnt1s = [0] * (l + 1)
        for i, v in enumerate(S):
            cnt1s[i + 1] = cnt1s[i] + (1 if v == '1' else 0)
        for i in range(l + 1):
            # 以 i 为分割线，把左边的1翻为0 + 把右边的0翻为1
            # 左边1的个数，需要翻为0
            left1 = cnt1s[i]
            # 右边0的个数，需要翻为1
            right0 = l - i - (cnt1s[l] - cnt1s[i])
            ret = min(ret, left1 + right0)
        return ret
