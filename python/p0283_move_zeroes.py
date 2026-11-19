"""LeetCode 283: https://leetcode.com/problems/move-zeroes/.

Stably compact nonzero values, then fill the suffix with zeroes in place.
O(n) time and O(1) extra space.
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        for index in range(write, len(nums)):
            nums[index] = 0
