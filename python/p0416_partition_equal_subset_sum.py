class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        reachable = 1
        mask = (1 << (target + 1)) - 1
        for value in nums:
            reachable = (reachable | (reachable << value)) & mask
        return bool(reachable & (1 << target))
