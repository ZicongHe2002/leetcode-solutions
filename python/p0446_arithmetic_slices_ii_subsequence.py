class Solution:
    def numberOfArithmeticSlices(self, nums):
        ending = [{} for _ in nums]
        total = 0
        for right, value in enumerate(nums):
            for left in range(right):
                difference = value - nums[left]
                extended = ending[left].get(difference, 0)
                total += extended
                ending[right][difference] = ending[right].get(difference, 0) + extended + 1
        return total
