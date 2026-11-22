class Solution:
    def smallestDivisor(self, nums, threshold):
        low, high = 1, max(nums)
        while low < high:
            middle = (low + high) // 2
            total = sum((value + middle - 1) // middle for value in nums)
            if total <= threshold:
                high = middle
            else:
                low = middle + 1
        return low
