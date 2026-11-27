class Solution:
    def movesToMakeZigzag(self, nums):
        costs = [0, 0]
        for index, value in enumerate(nums):
            left = nums[index - 1] if index else float('inf')
            right = nums[index + 1] if index + 1 < len(nums) else float('inf')
            costs[index % 2] += max(0, value - min(left, right) + 1)
        return min(costs)
