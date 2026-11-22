class Solution:
    def minCostConnectPoints(self, points):
        size = len(points)
        selected = [False] * size
        best = [4000001] * size
        best[0] = 0
        total = 0
        for _ in range(size):
            node = min((candidate for candidate in range(size) if not selected[candidate]),
                       key=best.__getitem__)
            selected[node] = True
            total += best[node]
            x, y = points[node]
            for target in range(size):
                if not selected[target]:
                    distance = abs(x - points[target][0]) + abs(y - points[target][1])
                    if distance < best[target]:
                        best[target] = distance
        return total
