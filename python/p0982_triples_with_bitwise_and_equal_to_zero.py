class Solution:
    def countTriplets(self, nums):
        bits = max(nums).bit_length()
        limit = 1 << bits
        subset = [0] * limit
        for first in nums:
            for second in nums:
                subset[first & second] += 1
        step = 1
        while step < limit:
            for start in range(0,limit,2 * step):
                for offset in range(step):
                    subset[start + step + offset] += subset[start + offset]
            step *= 2
        full = limit - 1
        return sum(subset[full ^ value] for value in nums)
