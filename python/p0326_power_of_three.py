class Solution:
    def isPowerOfThree(self, n):
        # 3**19 is the largest power of three in the signed 32-bit input range.
        return n > 0 and 1162261467 % n == 0
