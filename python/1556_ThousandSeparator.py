class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        ret = ""
        while n > 0:
            c, n = n % 1000, n // 1000
            if n == 0:
                ret = "{}{}".format(c, ret)
            else:
                ret = ".{:03d}{}".format(c, ret)

        return ret
