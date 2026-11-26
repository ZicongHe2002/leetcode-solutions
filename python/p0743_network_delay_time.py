from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times, n, k):
        outgoing = [[] for _ in range(n + 1)]
        for first, second, weight in times:
            outgoing[first].append((second, weight))
        infinity = float('inf')
        distance = [infinity] * (n + 1)
        distance[k] = 0
        pending = [(0, k)]
        while pending:
            elapsed, node = heappop(pending)
            if elapsed != distance[node]:
                continue
            for following, weight in outgoing[node]:
                candidate = elapsed + weight
                if candidate < distance[following]:
                    distance[following] = candidate
                    heappush(pending, (candidate, following))
        result = max(distance[1:])
        return -1 if result == infinity else result
