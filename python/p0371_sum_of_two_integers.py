class Solution:
    def getSum(self, a, b):
        mask = 0xffffffff
        sign = 0x80000000
        a &= mask
        b &= mask
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a < sign else ~(a ^ mask)
