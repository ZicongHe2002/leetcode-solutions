from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        edges = [[[] for _ in range(n)] for _ in range(2)]
        for color, pairs in enumerate((redEdges, blueEdges)):
            for start, end in pairs:
                edges[color][start].append(end)
        distance = [[-1, -1] for _ in range(n)]
        distance[0] = [0, 0]
        pending = deque(((0, 0), (0, 1)))
        while pending:
            node, previous = pending.popleft()
            color = 1 - previous
            for following in edges[color][node]:
                if distance[following][color] == -1:
                    distance[following][color] = distance[node][previous] + 1
                    pending.append((following, color))
        return [min(value for value in pair if value >= 0) if max(pair) >= 0 else -1
                for pair in distance]
