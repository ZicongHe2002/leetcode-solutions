class Solution:
    def largestPerimeter(self, nums):
        values = sorted(nums)
        for last in range(len(values) - 1,1,-1):
            if values[last - 2] + values[last - 1] > values[last]:
                return values[last - 2] + values[last - 1] + values[last]
        return 0
