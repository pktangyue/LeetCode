class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        # 一位数的情况，个数为10个
        ret = 10
        # 二位数、三位数、直到 n 位数
        for i in range(2, n + 1):
            # 第一位只能是 1-9
            cnt = 9
            # 从第二位开始，可取数字为9，后面依次减1
            for j in range(1, i):
                cnt *= 10 - j
            ret += cnt

        return ret
