from collections import Counter
from heapq import heappush, heappushpop


class _Entry:
    def __init__(self, word, frequency):
        self.word, self.frequency = word, frequency

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency < other.frequency
        return self.word > other.word


class Solution:
    def topKFrequent(self, words, k):
        heap = []
        for word, frequency in Counter(words).items():
            entry = _Entry(word, frequency)
            if len(heap) < k:
                heappush(heap, entry)
            else:
                heappushpop(heap, entry)
        return [entry.word for entry in sorted(heap, key=lambda item: (-item.frequency, item.word))]
