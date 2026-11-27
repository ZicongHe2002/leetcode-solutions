from collections import deque


class Solution:
    def possibleBipartition(self, n, dislikes):
        graph = [[] for _ in range(n + 1)]
        for first, second in dislikes:
            graph[first].append(second)
            graph[second].append(first)
        color = [0] * (n + 1)
        for start in range(1, n + 1):
            if color[start]:
                continue
            color[start] = 1
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not color[neighbor]:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True
