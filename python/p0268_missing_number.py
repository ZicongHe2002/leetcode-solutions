class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for index, value in enumerate(nums):
            missing ^= index ^ value
        return missing
