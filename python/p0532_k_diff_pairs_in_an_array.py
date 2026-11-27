from collections import Counter


class Solution:
    def findPairs(self, nums, k):
        counts = Counter(nums)
        if k == 0:
            return sum(frequency >= 2 for frequency in counts.values())
        return sum(value + k in counts for value in counts)
