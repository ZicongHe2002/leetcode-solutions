class Solution:
    def maxWidthRamp(self, nums):
        starts = []
        for index,value in enumerate(nums):
            if not starts or value < nums[starts[-1]]:
                starts.append(index)
        best = 0
        for right in range(len(nums) - 1,-1,-1):
            while starts and nums[starts[-1]] <= nums[right]:
                best = max(best,right - starts.pop())
        return best
