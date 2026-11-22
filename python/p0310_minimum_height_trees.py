from collections import deque


class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        neighbors = [[] for _ in range(n)]
        for left, right in edges:
            neighbors[left].append(right)
            neighbors[right].append(left)
        degree = [len(adjacent) for adjacent in neighbors]
        leaves = deque(node for node, count in enumerate(degree) if count == 1)
        remaining = n
        while remaining > 2:
            layer_size = len(leaves)
            remaining -= layer_size
            for _ in range(layer_size):
                leaf = leaves.popleft()
                for neighbor in neighbors[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)
