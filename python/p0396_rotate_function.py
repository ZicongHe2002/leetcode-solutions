class Solution:
    def maxRotateFunction(self, nums):
        size = len(nums)
        total = sum(nums)
        weighted = sum(index * value for index, value in enumerate(nums))
        best = weighted
        for index in range(size - 1, 0, -1):
            weighted += total - size * nums[index]
            best = max(best, weighted)
        return best
