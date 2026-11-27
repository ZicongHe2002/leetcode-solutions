from collections import Counter


class Solution:
    def findLHS(self, nums):
        counts = Counter(nums)
        return max((count + counts[value + 1] for value, count in counts.items()
                    if value + 1 in counts), default=0)
