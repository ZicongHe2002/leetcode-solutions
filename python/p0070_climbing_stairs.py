"""LeetCode 70: https://leetcode.com/problems/climbing-stairs/.

Count ordered one-step/two-step paths with constant extra space.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        previous, current = 1, 1
        for _ in range(n):
            previous, current = current, previous + current
        return previous
