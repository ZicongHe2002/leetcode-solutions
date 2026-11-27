class Solution:
    def sumOfDigits(self, nums):
        value = min(nums)
        total = 0
        while value:
            total += value % 10
            value //= 10
        return int(total % 2 == 0)
