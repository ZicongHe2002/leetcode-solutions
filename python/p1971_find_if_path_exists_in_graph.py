class Solution:
    def validPath(self, n, edges, source, destination):
        neighbors = [[] for _ in range(n)]
        for left, right in edges:
            neighbors[left].append(right)
            neighbors[right].append(left)
        seen = [False] * n
        seen[source] = True
        pending = [source]
        while pending:
            node = pending.pop()
            if node == destination:
                return True
            for successor in neighbors[node]:
                if not seen[successor]:
                    seen[successor] = True
                    pending.append(successor)
        return False
