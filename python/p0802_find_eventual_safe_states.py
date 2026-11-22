from collections import deque


class Solution:
    def eventualSafeNodes(self, graph):
        predecessors = [[] for _ in graph]
        remaining = [len(neighbors) for neighbors in graph]
        for node, neighbors in enumerate(graph):
            for successor in neighbors:
                predecessors[successor].append(node)
        pending = deque(node for node, degree in enumerate(remaining) if degree == 0)
        while pending:
            node = pending.popleft()
            for predecessor in predecessors[node]:
                remaining[predecessor] -= 1
                if remaining[predecessor] == 0:
                    pending.append(predecessor)
        return [node for node, degree in enumerate(remaining) if degree == 0]
