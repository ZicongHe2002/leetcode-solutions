class Solution:
    def trailingZeroes(self, n):
        zeroes = 0
        while n:
            n //= 5
            zeroes += n
        return zeroes
