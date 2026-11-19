"""LeetCode 26: https://leetcode.com/problems/remove-duplicates-from-sorted-array/.

Compact the distinct sorted values into the same list's prefix.
O(n) time and O(1) extra space; values beyond the returned length are unspecified.
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write
