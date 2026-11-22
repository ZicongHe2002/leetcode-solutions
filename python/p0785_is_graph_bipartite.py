class Solution:
    def isBipartite(self, graph):
        colors = [-1] * len(graph)
        for start in range(len(graph)):
            if colors[start] != -1:
                continue
            colors[start] = 0
            pending = [start]
            while pending:
                node = pending.pop()
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        pending.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
        return True
