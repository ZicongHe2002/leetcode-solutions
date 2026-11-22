class Solution:
    def hasAlternatingBits(self, n):
        adjacent_difference = n ^ (n >> 1)
        return adjacent_difference & (adjacent_difference + 1) == 0
