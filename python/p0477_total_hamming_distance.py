class Solution:
    def totalHammingDistance(self, nums):
        total = 0
        size = len(nums)
        for bit in range(max(nums, default=0).bit_length()):
            ones = sum((value >> bit) & 1 for value in nums)
            total += ones * (size - ones)
        return total
