class Solution:
    def findLengthOfLCIS(self, nums):
        ending = best = 0
        for index, value in enumerate(nums):
            ending = ending + 1 if index and nums[index - 1] < value else 1
            best = max(best, ending)
        return best
