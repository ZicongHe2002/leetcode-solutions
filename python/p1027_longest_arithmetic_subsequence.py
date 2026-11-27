class Solution:
    def longestArithSeqLength(self, nums):
        ending = [{} for _ in nums]
        longest = 2
        for right in range(len(nums)):
            for left in range(right):
                difference = nums[right] - nums[left]
                extended = ending[left].get(difference, 1) + 1
                if extended > ending[right].get(difference, 0):
                    ending[right][difference] = extended
                longest = max(longest, extended)
        return longest
