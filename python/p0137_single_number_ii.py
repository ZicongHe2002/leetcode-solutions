class Solution:
    def singleNumber(self, nums):
        once = twice = 0
        for value in nums:
            once = (once ^ value) & ~twice
            twice = (twice ^ value) & ~once
        return once
