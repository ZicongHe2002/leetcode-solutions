class Solution:
    def minMoves2(self, nums):
        ordered = sorted(nums)
        median = ordered[len(ordered) // 2]
        return sum(abs(value - median) for value in nums)
