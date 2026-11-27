class Solution:
    def isIdealPermutation(self, nums):
        largest = -1
        for index in range(2, len(nums)):
            largest = max(largest, nums[index - 2])
            if largest > nums[index]:
                return False
        return True
