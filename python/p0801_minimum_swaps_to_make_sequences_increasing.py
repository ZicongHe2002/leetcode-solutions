class Solution:
    def minSwap(self, nums1, nums2):
        size = len(nums1)
        keep, swap = 0, 1
        for index in range(1,size):
            next_keep = next_swap = size + 1
            if nums1[index - 1] < nums1[index] and nums2[index - 1] < nums2[index]:
                next_keep = min(next_keep,keep)
                next_swap = min(next_swap,swap + 1)
            if nums1[index - 1] < nums2[index] and nums2[index - 1] < nums1[index]:
                next_keep = min(next_keep,swap)
                next_swap = min(next_swap,keep + 1)
            keep, swap = next_keep, next_swap
        return min(keep,swap)
