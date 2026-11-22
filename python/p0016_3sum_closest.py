class Solution:
    def threeSumClosest(self, nums, target):
        values = sorted(nums)
        best = sum(values[:3])
        for first in range(len(values) - 2):
            left, right = first + 1, len(values) - 1
            while left < right:
                total = values[first] + values[left] + values[right]
                if abs(total - target) < abs(best - target):
                    best = total
                if total == target:
                    return total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return best
