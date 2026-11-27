class Solution:
    def dominantIndex(self, nums):
        largest = max(range(len(nums)), key=nums.__getitem__)
        return largest if all(nums[largest] >= 2 * value for index, value in enumerate(nums)
                              if index != largest) else -1
