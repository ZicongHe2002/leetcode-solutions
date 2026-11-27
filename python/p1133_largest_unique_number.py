from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums):
        return max((value for value, count in Counter(nums).items() if count == 1), default=-1)
