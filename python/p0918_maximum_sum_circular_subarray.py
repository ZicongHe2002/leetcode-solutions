class Solution:
    def maxSubarraySumCircular(self, nums):
        total = current_max = best_max = current_min = best_min = nums[0]
        for index in range(1,len(nums)):
            value = nums[index]
            total += value
            current_max = max(value,current_max + value)
            best_max = max(best_max,current_max)
            current_min = min(value,current_min + value)
            best_min = min(best_min,current_min)
        if best_max < 0:
            return best_max
        return max(best_max,total - best_min)
