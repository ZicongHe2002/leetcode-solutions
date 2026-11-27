class Solution:
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        remaining = set(nums1)
        result = []
        for value in nums2:
            if value in remaining:
                result.append(value)
                remaining.remove(value)
        return result
