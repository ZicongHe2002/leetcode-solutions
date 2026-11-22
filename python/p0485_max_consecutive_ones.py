class Solution:
    def findMaxConsecutiveOnes(self, nums):
        run = best = 0
        for value in nums:
            run = run + 1 if value == 1 else 0
            best = max(best, run)
        return best
