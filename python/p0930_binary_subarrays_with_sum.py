class Solution:
    def numSubarraysWithSum(self, nums, goal):
        def at_most(budget):
            if budget < 0:
                return 0
            left = total = result = 0
            for right, value in enumerate(nums):
                total += value
                while total > budget:
                    total -= nums[left]
                    left += 1
                result += right - left + 1
            return result

        return at_most(goal) - at_most(goal - 1)
