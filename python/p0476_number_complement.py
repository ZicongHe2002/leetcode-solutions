class Solution:
    def findComplement(self, num):
        next_power = 1
        while next_power <= num:
            next_power <<= 1
        return (next_power - 1) ^ num
