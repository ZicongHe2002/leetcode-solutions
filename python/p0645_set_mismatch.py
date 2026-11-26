class Solution:
    def findErrorNums(self, nums):
        difference = 0
        for expected, actual in enumerate(nums, 1):
            difference ^= expected ^ actual
        distinguishing_bit = difference & -difference
        first = 0
        for expected, actual in enumerate(nums, 1):
            if expected & distinguishing_bit:
                first ^= expected
            if actual & distinguishing_bit:
                first ^= actual
        second = difference ^ first
        return [first, second] if first in nums else [second, first]
