class Solution:
    def subarraysDivByK(self, nums, k):
        counts = [0] * k
        counts[0] = 1
        remainder = result = 0
        for value in nums:
            remainder = (remainder + value) % k
            result += counts[remainder]
            counts[remainder] += 1
        return result
