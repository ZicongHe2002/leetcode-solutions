"""LeetCode 198: https://leetcode.com/problems/house-robber/.

Return the largest non-adjacent sum without modifying the input.
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        previous, current = 0, 0
        for amount in nums:
            previous, current = current, max(current, previous + amount)
        return current
