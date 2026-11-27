from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s):
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2:
            return ''
        heap = [(-count, char) for char, count in counts.items()]
        heapify(heap)
        previous_count, previous_char = 0, ''
        result = []
        while heap:
            count, char = heappop(heap)
            result.append(char)
            if previous_count < 0:
                heappush(heap, (previous_count, previous_char))
            previous_count, previous_char = count + 1, char
        return ''.join(result)
