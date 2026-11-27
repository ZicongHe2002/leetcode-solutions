class Solution:
    def arrayPairSum(self, nums):
        ordered = sorted(nums)
        return sum(ordered[::2])
