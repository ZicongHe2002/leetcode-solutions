class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        best = [0] * (len(nums2) + 1)
        for value in nums1:
            diagonal = 0
            for column in range(1,len(nums2) + 1):
                previous = best[column]
                if value == nums2[column - 1]:
                    best[column] = diagonal + 1
                else:
                    best[column] = max(best[column],best[column - 1])
                diagonal = previous
        return best[-1]
