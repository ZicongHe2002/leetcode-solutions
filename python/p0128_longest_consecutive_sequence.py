class Solution:
    def longestConsecutive(self, nums):
        values = set(nums)
        best = 0
        for start in values:
            if start - 1 in values:
                continue
            length = 1
            while start + length in values:
                length += 1
            best = max(best, length)
        return best
