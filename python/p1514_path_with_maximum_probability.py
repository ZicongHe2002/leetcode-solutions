import heapq


class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        neighbors = [[] for _ in range(n)]
        for (left, right), probability in zip(edges, succProb):
            neighbors[left].append((right, probability))
            neighbors[right].append((left, probability))
        best = [0.0] * n
        best[start_node] = 1.0
        pending = [(-1.0, start_node)]
        while pending:
            negative, node = heapq.heappop(pending)
            probability = -negative
            if probability < best[node]:
                continue
            if node == end_node:
                return probability
            for target, chance in neighbors[node]:
                candidate = probability * chance
                if candidate > best[target]:
                    best[target] = candidate
                    heapq.heappush(pending, (-candidate, target))
        return 0.0
