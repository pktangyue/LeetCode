class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        prefix = ""
        if num < 0:
            prefix = "-"
            num = -num
        nums = []
        while not (-7 < num < 7):
            num, remain = num // 7, num % 7
            nums.insert(0, remain)

        if num:
            nums.insert(0, num)

        return prefix + "".join(map(str, nums))
