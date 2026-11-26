from heapq import heappop, heappush


class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))
        available = []
        index = 0
        for _ in range(min(k, len(projects))):
            while index < len(projects) and projects[index][0] <= w:
                heappush(available, -projects[index][1])
                index += 1
            if not available:
                break
            w -= heappop(available)
        return w
