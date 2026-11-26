class Solution:
    def minPatches(self, nums, n):
        missing = 1
        index = patches = 0
        while missing <= n:
            if index < len(nums) and nums[index] <= missing:
                missing += nums[index]
                index += 1
            else:
                missing += missing
                patches += 1
        return patches
