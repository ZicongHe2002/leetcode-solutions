class Solution:
    def reorderedPowerOf2(self, n):
        digits = sorted(str(n))
        return any(sorted(str(1 << exponent)) == digits for exponent in range(31))
