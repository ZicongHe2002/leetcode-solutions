class Solution:
    def baseNeg2(self, n):
        if n == 0:
            return '0'
        digits = []
        while n:
            bit = n & 1
            digits.append(str(bit))
            n = (n - bit) // -2
        return ''.join(reversed(digits))
