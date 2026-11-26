class Solution:
    def findMaxAverage(self, nums, k):
        total = sum(nums[index] for index in range(k))
        best = total
        for index in range(k, len(nums)):
            total += nums[index] - nums[index - k]
            best = max(best, total)
        return best / k
