import heapq


class Solution:
    def lastStoneWeight(self, stones):
        heap = [-weight for weight in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap,second - first)
        return -heap[0] if heap else 0
