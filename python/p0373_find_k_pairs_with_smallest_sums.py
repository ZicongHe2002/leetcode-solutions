from heapq import heapify, heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        pending = [(nums1[row] + nums2[0], row, 0) for row in range(min(k, len(nums1)))]
        heapify(pending)
        result = []
        for _ in range(k):
            _, row, column = heappop(pending)
            result.append([nums1[row], nums2[column]])
            if column + 1 < len(nums2):
                column += 1
                heappush(pending, (nums1[row] + nums2[column], row, column))
        return result
