class Solution:
    def combinationSum4(self, nums, target):
        counts = [0] * (target + 1)
        counts[0] = 1
        for total in range(1, target + 1):
            for value in nums:
                if value <= total:
                    counts[total] += counts[total - value]
        return counts[target]
