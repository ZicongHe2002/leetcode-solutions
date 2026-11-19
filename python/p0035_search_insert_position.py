"""LeetCode 35: https://leetcode.com/problems/search-insert-position/.

Find the first position whose value is not less than target in O(log n) time.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left
