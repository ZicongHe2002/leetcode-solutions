class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for index, value in enumerate(nums):
            if left == total - left - value:
                return index
            left += value
        return -1
