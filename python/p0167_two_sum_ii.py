"""LeetCode 167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/.

Return one-based distinct indices in a sorted array in O(n) time, O(1) space.
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1
        raise ValueError("No pair of distinct indices sums to target")
