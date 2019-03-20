class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while True:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            if b == 0:
                break
        return a if a <= MAX else ~(a ^ mask)
