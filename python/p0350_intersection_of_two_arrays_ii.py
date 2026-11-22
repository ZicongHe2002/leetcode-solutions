from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        remaining = Counter(nums1)
        result = []
        for value in nums2:
            if remaining[value] > 0:
                result.append(value)
                remaining[value] -= 1
        return result
