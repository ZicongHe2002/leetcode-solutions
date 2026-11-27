class Solution:
    def firstMissingPositive(self, nums):
        size = len(nums)
        for index in range(size):
            while 1 <= nums[index] <= size:
                destination = nums[index] - 1
                if nums[destination] == nums[index]:
                    break
                nums[index], nums[destination] = nums[destination], nums[index]
        for index, value in enumerate(nums):
            if value != index + 1:
                return index + 1
        return size + 1
