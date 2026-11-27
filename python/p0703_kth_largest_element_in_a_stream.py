from heapq import heapify, heappush, heappushpop, nlargest


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nlargest(k, nums)
        heapify(self.heap)

    def add(self, val):
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)
        return self.heap[0]
