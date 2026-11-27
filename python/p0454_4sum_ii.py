from collections import Counter


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        first_pairs = Counter(first + second for first in nums1 for second in nums2)
        return sum(first_pairs.get(-third - fourth, 0) for third in nums3 for fourth in nums4)
