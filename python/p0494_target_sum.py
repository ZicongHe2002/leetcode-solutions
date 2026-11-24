class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        if abs(target) > total or (total + target) % 2:
            return 0
        capacity = (total + target) // 2
        counts = [0] * (capacity + 1)
        counts[0] = 1
        for value in nums:
            for subtotal in range(capacity, value - 1, -1):
                counts[subtotal] += counts[subtotal - value]
        return counts[capacity]
