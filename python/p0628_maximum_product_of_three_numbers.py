class Solution:
    def maximumProduct(self, nums):
        first = sorted(nums[:3])
        low1, low2 = first[:2]
        high3, high2, high1 = first
        for index in range(3, len(nums)):
            value = nums[index]
            if value >= high1:
                high3, high2, high1 = high2, high1, value
            elif value >= high2:
                high3, high2 = high2, value
            elif value > high3:
                high3 = value
            if value <= low1:
                low1, low2 = value, low1
            elif value < low2:
                low2 = value
        return max(high1 * high2 * high3, high1 * low1 * low2)
