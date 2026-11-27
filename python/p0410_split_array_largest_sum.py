class Solution:
    def splitArray(self, nums, k):
        low, high = max(nums), sum(nums)
        while low < high:
            limit = (low + high) // 2
            groups = 1
            subtotal = 0
            for value in nums:
                if subtotal + value > limit:
                    groups += 1
                    subtotal = value
                else:
                    subtotal += value
            if groups <= k:
                high = limit
            else:
                low = limit + 1
        return low
