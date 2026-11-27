class Solution:
    def missingElement(self, nums, k):
        left,right = 0,len(nums)
        while left < right:
            middle = (left + right) // 2
            missing = nums[middle] - nums[0] - middle
            if missing >= k:
                right = middle
            else:
                left = middle + 1
        return nums[0] + k + left - 1
