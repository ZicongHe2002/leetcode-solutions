class Solution:
    def sortArrayByParity(self, nums):
        return [value for value in nums if value % 2 == 0] + [value for value in nums if value % 2]
