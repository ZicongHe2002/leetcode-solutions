class Solution:
    def hammingDistance(self, x, y):
        difference = x ^ y
        count = 0
        while difference:
            difference &= difference - 1
            count += 1
        return count
