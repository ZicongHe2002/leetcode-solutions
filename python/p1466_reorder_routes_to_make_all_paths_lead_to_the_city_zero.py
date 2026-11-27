class Solution:
    def minReorder(self, n, connections):
        neighbors = [[] for _ in range(n)]
        for source, target in connections:
            neighbors[source].append((target, 1))
            neighbors[target].append((source, 0))
        pending = [(0, -1)]
        changed = 0
        while pending:
            node, parent = pending.pop()
            for successor, points_away in neighbors[node]:
                if successor != parent:
                    changed += points_away
                    pending.append((successor, node))
        return changed
