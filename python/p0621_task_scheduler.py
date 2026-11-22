from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        if not tasks:
            return 0
        counts = Counter(tasks)
        largest = max(counts.values())
        tied = sum(count == largest for count in counts.values())
        return max(len(tasks), (largest - 1) * (n + 1) + tied)
