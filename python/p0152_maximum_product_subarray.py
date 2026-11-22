class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        smallest = largest = best = nums[0]
        for index in range(1, len(nums)):
            value = nums[index]
            low_product = value * smallest
            high_product = value * largest
            smallest = min(value, low_product, high_product)
            largest = max(value, low_product, high_product)
            best = max(best, largest)
        return best
