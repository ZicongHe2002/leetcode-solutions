from fractions import Fraction
import heapq


class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        order = sorted(range(len(quality)),key=lambda index:Fraction(wage[index],quality[index]))
        heap = []
        total_quality = 0
        best = None
        for index in order:
            heapq.heappush(heap,-quality[index])
            total_quality += quality[index]
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
            if len(heap) == k:
                cost = Fraction(total_quality * wage[index],quality[index])
                if best is None or cost < best:
                    best = cost
        return float(best)
