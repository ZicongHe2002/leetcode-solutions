class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        if max(nums) > target:
            return False
        remainders = [-1] * (1 << len(nums))
        remainders[0] = 0
        for mask, current in enumerate(remainders):
            if current < 0:
                continue
            for index, value in enumerate(nums):
                bit = 1 << index
                if not mask & bit and current + value <= target:
                    remainders[mask | bit] = (current + value) % target
        return remainders[-1] == 0
