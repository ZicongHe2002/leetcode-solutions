class Solution:
    def searchRange(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        first = left
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        right = len(nums)
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle
        return [first, left - 1]
