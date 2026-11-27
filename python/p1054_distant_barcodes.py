from collections import Counter
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes):
        heap = [(-count,value) for value,count in Counter(barcodes).items()]
        heapq.heapify(heap)
        previous_count = 0
        previous_value = None
        result = []
        while heap:
            count,value = heapq.heappop(heap)
            result.append(value)
            count += 1
            if previous_count < 0:
                heapq.heappush(heap,(previous_count,previous_value))
            previous_count,previous_value = count,value
        return result
