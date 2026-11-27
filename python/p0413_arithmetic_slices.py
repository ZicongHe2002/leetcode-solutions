class Solution:
    def numberOfArithmeticSlices(self, nums):
        ending = total = 0
        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                ending += 1
            else:
                ending = 0
            total += ending
        return total
