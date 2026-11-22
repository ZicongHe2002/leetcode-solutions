class Solution:
    def subarraySum(self, nums, k):
        counts = {0: 1}
        prefix = result = 0
        for value in nums:
            prefix += value
            result += counts.get(prefix - k, 0)
            counts[prefix] = counts.get(prefix, 0) + 1
        return result
