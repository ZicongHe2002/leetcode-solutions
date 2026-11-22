class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left = result = 0
        product = 1
        for right, value in enumerate(nums):
            product *= value
            while product >= k:
                product //= nums[left]
                left += 1
            result += right - left + 1
        return result
