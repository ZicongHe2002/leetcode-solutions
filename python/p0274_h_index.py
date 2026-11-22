class Solution:
    def hIndex(self, citations):
        size = len(citations)
        counts = [0] * (size + 1)
        for value in citations:
            counts[min(value, size)] += 1
        papers = 0
        for h in range(size, -1, -1):
            papers += counts[h]
            if papers >= h:
                return h
