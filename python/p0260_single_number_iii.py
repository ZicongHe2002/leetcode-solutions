class Solution:
    def singleNumber(self, nums):
        combined = 0
        for value in nums:
            combined ^= value
        differing_bit = combined & -combined
        first = 0
        for value in nums:
            if value & differing_bit:
                first ^= value
        return [first, combined ^ first]
