from heapq import heapify, heappop, heappush


class Solution:
    def minBuildTime(self, blocks, split):
        pending = list(blocks)
        heapify(pending)
        while len(pending) > 1:
            first = heappop(pending)
            second = heappop(pending)
            heappush(pending, max(first, second) + split)
        return pending[0]
