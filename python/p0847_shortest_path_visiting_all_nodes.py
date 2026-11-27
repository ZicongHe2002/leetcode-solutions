from collections import deque


class Solution:
    def shortestPathLength(self, graph):
        size = len(graph)
        if size == 1:
            return 0
        full = (1 << size) - 1
        queue = deque((node,1 << node,0) for node in range(size))
        seen = {(node,1 << node) for node in range(size)}
        while queue:
            node,mask,distance = queue.popleft()
            for following in graph[node]:
                visited = mask | (1 << following)
                if visited == full:
                    return distance + 1
                state = following,visited
                if state not in seen:
                    seen.add(state)
                    queue.append((following,visited,distance + 1))
        return -1
