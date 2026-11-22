from heapq import heapify, heapreplace
from itertools import islice


class Solution:
    def findKthLargest(self, nums, k):
        values = iter(nums)
        selected = list(islice(values, k))
        heapify(selected)
        for value in values:
            if value > selected[0]:
                heapreplace(selected, value)
        return selected[0]
