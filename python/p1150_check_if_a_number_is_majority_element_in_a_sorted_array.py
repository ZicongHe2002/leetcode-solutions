from bisect import bisect_left, bisect_right


class Solution:
    def isMajorityElement(self, nums, target):
        return bisect_right(nums, target) - bisect_left(nums, target) > len(nums) // 2
