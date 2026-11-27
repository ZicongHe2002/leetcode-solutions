class Solution:
    def canDivideIntoSubsequences(self, nums, k):
        maximum = run = 0
        previous = None
        for value in nums:
            run = run + 1 if value == previous else 1
            maximum = max(maximum, run)
            previous = value
        return maximum * k <= len(nums)
