class Solution:
    def findLength(self, nums1, nums2):
        suffix = [0] * (len(nums2) + 1)
        best = 0
        for first in nums1:
            for j in range(len(nums2), 0, -1):
                suffix[j] = suffix[j - 1] + 1 if first == nums2[j - 1] else 0
                best = max(best, suffix[j])
        return best
