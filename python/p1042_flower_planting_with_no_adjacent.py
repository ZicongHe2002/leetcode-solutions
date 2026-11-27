class Solution:
    def gardenNoAdj(self, n, paths):
        neighbors = [[] for _ in range(n)]
        for left, right in paths:
            neighbors[left - 1].append(right - 1)
            neighbors[right - 1].append(left - 1)
        colors = [0] * n
        for garden in range(n):
            used = {colors[neighbor] for neighbor in neighbors[garden]}
            colors[garden] = next(color for color in range(1, 5) if color not in used)
        return colors
