class Solution:
    def findDisappearedNumbers(self, nums):
        for value in nums:
            position = abs(value) - 1
            if nums[position] > 0:
                nums[position] = -nums[position]
        missing = []
        for index, value in enumerate(nums):
            if value > 0:
                missing.append(index + 1)
            nums[index] = abs(value)
        return missing
